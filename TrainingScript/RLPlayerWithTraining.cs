public class RLPlayerWithTraining : Player
{
    private float alpha = 0.01f; // Learning rate (reduced)
    private float gamma = 0.95f; // Discount factor (increased)
    private float epsilon = 1.0f; // Initial exploration rate
    private float epsilonDecay = 0.99995f; // Epsilon decay rate
    private float finalEpsilon = 0.1f; // Final exploration rate

    private string qTableFilePath = "/qtable2.json"; // Path to save the qTable
    private (int, int, bool) lastState;
    private int lastAction;
    private Random random = new Random();

    private float[,,,] qTable = new float[33, 12, 2, 2]; // (Player sum, Dealer card, Usable ace, Action)

    public RLPlayerWithTraining()
    {
        LoadQTable();
    }

	static void PrintQTable(float[,,,] qTable)
	{
		string[] aceStatus = { "Without Usable Ace", "With Usable Ace" };

		for (int ace = 0; ace < 2; ace++)
		{
			Console.WriteLine($"\n{aceStatus[ace]}:");

			// Print header
			Console.Write("     ");
			for (int dealerCard = 1; dealerCard <= 11; dealerCard++)
			{
				Console.Write($"{dealerCard,6}");
			}

			Console.WriteLine("\n" + new string('-', 80));

			// Print table contents
			for (int playerSum = 4; playerSum <= 21; playerSum++)
			{
				Console.Write($"{playerSum,2} |");
				for (int dealerCard = 1; dealerCard <= 11; dealerCard++)
				{
					float qValueHit = qTable[playerSum, dealerCard, ace, 1];
					float qValueStand = qTable[playerSum, dealerCard, ace, 0];

					if (qValueHit == 0 && qValueStand == 0)
					{
						Console.Write($"  U  "); // Unencountered state
					}
					else if (qValueHit > qValueStand)
					{
						Console.Write($"  H  "); // Hit is better
					}
					else
					{
						Console.Write($"  S  "); // Stand is better
					}
				}
				Console.WriteLine();
			}
			Console.WriteLine();
		}
	}


	public void SaveQTable()
	{
		var qTableList = new List<float>();
		for (int i = 0; i < 33; i++)
		{
			for (int j = 0; j < 12; j++)
			{
				for (int k = 0; k < 2; k++)
				{
					for (int l = 0; l < 2; l++)
					{
						qTableList.Add(qTable[i, j, k, l]);
					}
				}
			}
		}

		var json = JsonConvert.SerializeObject(qTableList, Formatting.Indented);
		File.WriteAllText(qTableFilePath, json);
	}

	public void LoadQTable()
	{
		if (File.Exists(qTableFilePath))
		{
			var json = File.ReadAllText(qTableFilePath);
			var qTableList = JsonConvert.DeserializeObject<List<float>>(json);
			int index = 0;

			for (int i = 0; i < 33; i++)
			{
				for (int j = 0; j < 12; j++)
				{
					for (int k = 0; k < 2; k++)
					{
						for (int l = 0; l < 2; l++)
						{
							qTable[i, j, k, l] = qTableList[index++];
						}
					}
				}
			}
		}
	}

    public void Train(int episodes)
    {
        int wins = 0, losses = 0, draws = 0;
        for (int ep = 1; ep <= episodes; ep++)
        {
            GameManager.deck.Shuffle();
            GameManager.dealer.StartHand();
            StartHand();

            while (!isBusted && handValue < 21)
            {
                var currentState = GetState();
                int action = ChooseAction(currentState);
                lastState = currentState;
                lastAction = action;

                if (action == 0) // Stand
                    break;
                else // Hit
                    GetCard();

                var nextState = GetState();
                int reward = isBusted ? -1 : 0; // Immediate reward for busting

                UpdateStrategy(lastState, lastAction, reward, nextState, false);
            }

            if (!isBusted)
            {
                GameManager.dealer.PlayTurn();
                int finalReward = EvaluateGame();
                var finalState = GetState();
                UpdateStrategy(lastState, lastAction, finalReward, finalState, true);

                if (finalReward == 1) wins++;
                else if (finalReward == -1) losses++;
                else draws++;
            }
            else
            {
                losses++;
            }

            DecayEpsilon();

            if (ep % 100 == 0)
            {
                Console.WriteLine($"Games played: {ep}, Wins: {wins}, Losses: {losses}, Draws: {draws}, Win rate: {(float)wins / (wins + losses) * 100}%, Epsilon: {epsilon:F4}");
                SaveQTable();
            }
        }
        PrintQTable(qTable);
    }

    private void DecayEpsilon()
    {
        epsilon = Math.Max(finalEpsilon, epsilon * epsilonDecay);
    }

    private int ChooseAction((int, int, bool) state)
    {
        if (random.NextDouble() < epsilon)
            return random.Next(2); // 0: Stand, 1: Hit

        var actionValues = GetActionValues(state);
        return actionValues[0] > actionValues[1] ? 0 : 1;
    }

    private void UpdateStrategy((int, int, bool) state, int action, int reward, (int, int, bool) nextState, bool isFinal)
    {
        int playerSum = state.Item1;
        int dealerCard = state.Item2;
        int usableAce = state.Item3 ? 1 : 0;

        float oldQValue = qTable[playerSum, dealerCard, usableAce, action];
        float nextMaxQValue = isFinal ? 0 : Math.Max(qTable[nextState.Item1, nextState.Item2, nextState.Item3 ? 1 : 0, 0],
                                                     qTable[nextState.Item1, nextState.Item2, nextState.Item3 ? 1 : 0, 1]);

        qTable[playerSum, dealerCard, usableAce, action] =
            oldQValue + alpha * (reward + gamma * nextMaxQValue - oldQValue);
    }

	public string Play()
	{
		StartHand();
		int reward = 0;
		while (!isBusted && handValue < 21)
		{
			var currentState = GetState();
			int action = ChooseAction(currentState);
			lastState = currentState;
			lastAction = action;
			if (action == 0) // Stand
				break;
			else // Hit
				GetCard();

			if (isBusted) return "loss";
		}

		if (!isBusted)
		{
			GameManager.dealer.PlayTurn();
		}

		reward = EvaluateGame();
		if (reward == 1) return "win";
		if (reward == -1) return "loss";
		return "draw";
	}

	private int EvaluateGame()
	{
		if (isBusted) return -1;
		if (GameManager.dealer.isBusted || handValue > GameManager.dealer.handValue) return 1;
		if (handValue < GameManager.dealer.handValue) return -1;
		return 0;
	}

	private float[] GetActionValues((int, int, bool) state)
	{
		int playerSum = state.Item1;
		int dealerCard = state.Item2;
		int usableAce = state.Item3 ? 1 : 0;

		return new float[]
		{
			qTable[playerSum, dealerCard, usableAce, 0], // Value for Stand
			qTable[playerSum, dealerCard, usableAce, 1]  // Value for Hit
		};
	}

	private (int, int, bool) GetState()
	{
		int dealerCardValue = GameManager.dealer.GetFirstCardValue();
		bool hasUsableAce = aceList.Exists(c => c.GetValueOfCard() == 11) && handValue <= 21;
		return (handValue, dealerCardValue, hasUsableAce);
	}
}