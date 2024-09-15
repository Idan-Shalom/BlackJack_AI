using UnityEngine;
using UnityEngine.UI;

public class Player : Participant
{
    [SerializeField] private Text cashText;
    
    protected int dealerCard = -1; // set to -1 until player learns the value.
    
    private int money = 1000;

    public void AdjustMoneyBy(int amount)
    {
        money += amount;
        cashText.text = money + "$";
    }

    public int GetMoney()
    {
        return money;
    }

    public void LearnFirstDealerCard(int value)
    {
        dealerCard = value;
    }
}