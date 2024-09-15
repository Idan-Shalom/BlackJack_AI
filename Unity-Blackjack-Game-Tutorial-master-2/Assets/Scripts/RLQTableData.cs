using System.Collections.Generic;
using UnityEngine;

[CreateAssetMenu(fileName = "RLQTableData", menuName = "ScriptableObjects/RLQTableData", order = 1)]
public class RLQTableData : ScriptableObject
{
    [System.Serializable]
    public struct QState
    {
        public int handValue;
        public int dealerCardValue;
        public bool hasUsableAce;

        public QState(int handValue, int dealerCardValue, bool hasUsableAce)
        {
            this.handValue = handValue;
            this.dealerCardValue = dealerCardValue;
            this.hasUsableAce = hasUsableAce;
        }
    }

    [System.Serializable]
    public class QValueDictionary : Dictionary<int, float> { }

    [System.Serializable]
    public class QTableDictionary : Dictionary<QState, QValueDictionary> { }

    public QTableDictionary qTable = new QTableDictionary();
}