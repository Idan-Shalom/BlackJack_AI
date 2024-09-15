using System.Collections;
using System.Collections.Generic;
using System.IO;
using Random = System.Random;
using Newtonsoft.Json;

namespace BlackJackTry
{
    public class RL_Player_Q_learning : Player
    {
        private float alpha = 0.1f; // Learning rate
        private float gamma = 0.9f; // Discount factor
        private float epsilon = 0.1f; // Exploration rate
        
        private string qTableFilePath = "Assets/jsonLearning.json"; // Path to save the qTable
        private (int, int, bool) lastState;
        private int lastAction;
        private Random random = new Random();

        private float[,,,] qTable = new float[33, 12, 2, 2]; // (Player sum, Dealer card, Usable ace, Action)

        private void Awake()
        {
            LoadQTable();
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


        public override IEnumerator PlayTurn()
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
                    yield return GetCard();
            }
        }

        private int ChooseAction((int, int, bool) state)
        {
            if (random.NextDouble() < epsilon)
                return random.Next(2); // 0: Stand, 1: Hit

            var actionValues = GetActionValues(state);
            return actionValues[0] > actionValues[1] ? 0 : 1;
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
            int dealerCardValue = dealerCard;
            bool hasUsableAce = aceList.Exists(c => c.GetValueOfCard() == 11) && handValue <= 21;
            return (handValue, dealerCardValue, hasUsableAce);
        }
}

    }
