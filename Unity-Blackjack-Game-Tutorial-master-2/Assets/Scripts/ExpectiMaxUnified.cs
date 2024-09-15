// using System;
// using System.Collections;
// using UnityEngine;
//
// public class ExpectiMaxUnified : Player
//     {
//         private static readonly float[] CARD_PROBABILITIES = {
//             0f, 4f/52f, 4f/52f, 4f/52f, 4f/52f, 4f/52f, 4f/52f, 4f/52f, 4f/52f, 4f/52f, 16f/52f
//         };
//         
//         [System.Serializable]
//         public enum RiskPreference
//         {
//             RiskAverse,
//             RiskLoving,
//             RiskNeutral
//         }
//     
//         [SerializeField] private RiskPreference riskPreference = RiskPreference.RiskNeutral;
//     
//         public override IEnumerator PlayTurn()
//         {
//             while (!isBusted && handValue < 21)
//             {
//                 int dealerUpCard = dealerCard;
//                 bool hasUsableAce = aceList.Exists(c => c.GetValueOfCard() == 11) && handValue <= 21;
//     
//                 bool shouldHit = DecideAction(handValue, dealerUpCard, hasUsableAce);
//                 
//                 if (!shouldHit) break;
//                 
//                 yield return GetCard();
//             }
//         }
//         private bool DecideAction(int playerSum, int dealerCard, bool hasUsableAce)
//         {
//             bool toHit = false;
//             float StandVal = Expectimax(playerSum, dealerCard,  false);
//             int newPlayerSum = playerSum;
//             for (int i = 1; i < 11; i++)
//             {
//                 if (i == 1 && newPlayerSum + 11 <= 21)
//                 {
//                     newPlayerSum += 11;
//                 }
//                 else
//                 {
//                     newPlayerSum += i;
//                 }
//                 float hitVal = Expectimax(newPlayerSum, dealerCard,  true);
//                 if (hitVal > StandVal)
//                 {
//                     toHit = true;
//                     break;
//                 }
//             }
//             return toHit;
//         }
//         
//         
//     
//         private float Expectimax(int playerSum, int dealerSum, bool isMaximizer)
//         {
//             if (dealerSum >= 17 || playerSum > 21)
//             {
//                 return EvaluateHand(playerSum, dealerSum);
//             }
//         
//             if (isMaximizer)
//             {
//                 float val = float.MinValue;
//                 
//                 for (int i = 1; i < 11; i++)
//                 {
//                     float prob = CARD_PROBABILITIES[i];
//                     int newPlayerSum = playerSum;
//                     if (i == 1 && newPlayerSum + 11 <= 21)
//                     {
//                         newPlayerSum += 11;
//                     }
//                     else
//                     {
//                         newPlayerSum += i;
//                     }
//                     val = Math.Max(val, prob*Expectimax(newPlayerSum, dealerSum,  false)); // end of turn 
//                     if (newPlayerSum < 21)
//                     {
//                         val = Math.Max(val, prob*Expectimax(newPlayerSum, dealerSum,  true)); //take another card
//                     }
//                 }
//         
//                 return val;
//             }
//             else
//             {
//                 float expectedValue = 0f;
//                 for (int i = 1; i < 11; i++)
//                 {
//                     int newDealerSum = dealerSum;
//                     float prob = CARD_PROBABILITIES[i];
//                     if (i == 1 && newDealerSum + 11 <= 21)
//                     {
//                         newDealerSum += 11;
//                     }
//                     else
//                     {
//                         newDealerSum += i;
//                     }
//                     expectedValue += prob * Expectimax(playerSum, newDealerSum, false);
//                 }
//         
//                 return expectedValue;
//             }
//         }
//         
//     
//     
//     
//     private float EvaluateHand(int playerSum, int dealerSum)
//     {
//        
//         bool player_win = false;
//         const int BLACKJACK = 21;
//         int distance = Math.Abs(BLACKJACK - playerSum);
//     
//         // If player busts, return a large negative value (loss)
//         if (playerSum > BLACKJACK)
//         {
//             player_win = false;
//         }
//     
//         // If dealer busts, player wins, return a large positive value
//         else if (dealerSum > BLACKJACK)
//         {
//             player_win = true;
//         }
//     
//         // If neither busts, compare their sums
//         else if (playerSum > dealerSum)
//         {
//             player_win = true;  // Player wins
//         }
//         else if (playerSum < dealerSum)
//         {
//             player_win = false;  // Dealer wins
//         }
//     
//         float winVal = player_win ? distance: -distance;
//         switch (riskPreference)
//         {
//             case RiskPreference.RiskAverse:
//                 return (float)Math.Log(Math.Abs(winVal)) * Math.Sign(winVal);
//             case RiskPreference.RiskLoving:
//                 return (float)Math.Exp(Math.Abs(winVal)) * Math.Sign(winVal);
//             case RiskPreference.RiskNeutral:
//             default:
//                 return winVal ;
//         }
//         
//     } 
// }


using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ExpectiMaxUnified : Player
{
    private static readonly float[] CARD_PROBABILITIES = {
        0f, 4f/52f, 4f/52f, 4f/52f, 4f/52f, 4f/52f, 4f/52f, 4f/52f, 4f/52f, 4f/52f, 16f/52f
    };
    [System.Serializable]
    public enum RiskPreference
    {
        RiskAverse,
        RiskLoving,
        RiskNeutral
    }
    
    [SerializeField] private RiskPreference riskPreference = RiskPreference.RiskNeutral;

    public int[,,,] decisionTable = new int[33, 12, 2, 2]; // (Player sum, Dealer card, Usable ace, Action)
    private Dictionary<(int, int, bool), float> memoTable = new Dictionary<(int, int, bool), float>();


    private void Awake()
    {
        // riskPreference = preference;
        // Initialize the decision table with -1 for "Unknown"
        for (int playerSum = 0; playerSum < 33; playerSum++)
        {
            for (int dealerCard = 0; dealerCard < 12; dealerCard++)
            {
                for (int usableAce = 0; usableAce < 2; usableAce++)
                {
                    for (int action = 0; action < 2; action++)
                    {
                        decisionTable[playerSum, dealerCard, usableAce, action] = -1; // Unknown
                    }
                }
            }
        }
    }

    public override IEnumerator PlayTurn()
    {
        while (!isBusted && handValue < 21)
        {
            int dealerUpCard = dealerCard;
            bool hasUsableAce = aceList.Exists(c => c.GetValueOfCard() == 11) && handValue <= 21;

            bool shouldHit = DecideAction(handValue, dealerUpCard, hasUsableAce);
            
            if (!shouldHit) break;
            
            yield return GetCard();
        }
    }
    
    private bool DecideAction(int playerSum, int dealerCard, bool hasUsableAce)
{
    bool toHit = false;
    float StandVal = expectimax(playerSum, dealerCard, false);
    float totalHitVal = 0f;
    float totalProb = 0f;

    for (int i = 1; i < 11; i++)
    {
        int newPlayerSum = playerSum;
        if (i == 1 && newPlayerSum + 11 <= 21)
        {
            newPlayerSum += 11;
        }
        else
        {
            newPlayerSum += i;
        }
        float hitVal = expectimax(newPlayerSum, dealerCard, true);
        float prob = CARD_PROBABILITIES[i];
        totalHitVal += hitVal * prob;
        totalProb += prob;
    }

    float averageHitVal = totalHitVal / totalProb;

    switch (riskPreference)
    {
        case RiskPreference.RiskLoving:
            // Risk-loving player will hit more often
            toHit = averageHitVal > StandVal - 5; // Lowered threshold for hitting
            break;
        case RiskPreference.RiskAverse:
            // Risk-averse player will hit less often
            toHit = averageHitVal > StandVal + 0.5;
            break;
        case RiskPreference.RiskNeutral:
        default:
            toHit = averageHitVal > StandVal;
            break;
    }

    int usableAce = hasUsableAce ? 1 : 0;
    decisionTable[playerSum, dealerCard, usableAce, 0] = toHit ? 1 : 0; // 0 for stand, 1 for hit
    return toHit;
}

private float EvaluateHand(int playerSum, int dealerSum)
{
    bool player_win = false;
    const int BLACKJACK = 21;
    int distance = Math.Abs(BLACKJACK - playerSum);

    if (playerSum > BLACKJACK)
    {
        player_win = false;
    }
    else if (dealerSum > BLACKJACK)
    {
        player_win = true;
    }
    else if (playerSum > dealerSum)
    {
        player_win = true;
    }
    else if (playerSum < dealerSum)
    {
        player_win = false;
    }

    float baseValue = player_win ? distance : -distance;

    switch (riskPreference)
    {
        case RiskPreference.RiskAverse:
            return (float)Math.Log(Math.Abs(baseValue) + 1) * Math.Sign(baseValue);
        case RiskPreference.RiskLoving:
            return (float)Math.Exp(Math.Abs(baseValue)) * Math.Sign(baseValue);
        case RiskPreference.RiskNeutral:
        default:
            return baseValue;
    }
}
    

    float expectimax(int playerSum, int dealerSum, bool isMaximizer)
    {
        var key = (playerSum, dealerSum, isMaximizer);
        if (memoTable.TryGetValue(key, out float cachedValue))
        {
            return cachedValue;
        }

        if (dealerSum >= 17 || playerSum > 21)
        {
            float result = EvaluateHand(playerSum, dealerSum);
            memoTable[key] = result;
            return result;
        }
    
        if (isMaximizer)
        {
            float val = float.MinValue;
            
            for (int i = 1; i < 11; i++)
            {
                float prob = CARD_PROBABILITIES[i];
                int newPlayerSum = playerSum;
                if (i == 1 && newPlayerSum + 11 <= 21)
                {
                    newPlayerSum += 11;
                }
                else
                {
                    newPlayerSum += i;
                }
                val = Math.Max(val, prob*expectimax(newPlayerSum, dealerSum,  false)); // end of turn 
                if (newPlayerSum < 21)
                {
                    val = Math.Max(val, prob*expectimax(newPlayerSum, dealerSum,  true)); //take another card
                }
            }
            memoTable[key] = val;
            return val;
        }
        else
        {
            float expectedValue = 0f;
            for (int i = 1; i < 11; i++)
            {
                int newDealerSum = dealerSum;
                float prob = CARD_PROBABILITIES[i];
                if (i == 1 && newDealerSum + 11 <= 21)
                {
                    newDealerSum += 11;
                }
                else
                {
                    newDealerSum += i;
                }
                expectedValue += prob * expectimax(playerSum, newDealerSum, false);
            }
            memoTable[key] = expectedValue;
            return expectedValue;
        }
    }

    

    public void PrintDecisionTable()
    {
        Console.WriteLine($"Decision Table for {riskPreference} Expectimax Player:");
        Console.WriteLine("S = Stand, H = Hit, U = Unknown");

        
        for (int ace = 0; ace <= 1; ace++)
        {
            int totalHits = 0;
            int totalStands = 0;
            int totalUnknown = 0;

            Console.WriteLine(ace == 0 ? "\nWithout Usable Ace:" : "\nWith Usable Ace:");
            Console.Write("Player Sum | ");
            for (int dealerCard = 1; dealerCard <= 11; dealerCard++)
            {
                Console.Write($"{dealerCard,2} ");
            }
            Console.WriteLine("\n-----------+--------------------------------");

            for (int playerSum = 4; playerSum <= 21; playerSum++)
            {
                Console.Write($"{playerSum,10} | ");
                for (int dealerCard = 1; dealerCard <= 11; dealerCard++)
                {
                    int decision = decisionTable[playerSum, dealerCard, ace, 0];
                    string decisionStr = decision == 1 ? "H" : (decision == 0 ? "S" : "U");
                    if (decision == 1) totalHits += 1;
                    if (decision == 0) totalStands += 1;
                    if (decision == -1) totalUnknown += 1;
                    
                    Console.Write($"{decisionStr,2} ");
                }
                Console.WriteLine();
            }
            Console.Write($"Total hits: {totalHits} ");
            Console.Write($"Total stands: {totalStands} ");
            Console.Write($"Total unknown: {totalUnknown} ");
            Console.WriteLine();
            Console.WriteLine();
        }
        
    }
   
}


