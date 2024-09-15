using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public abstract class Participant : MonoBehaviour
{
    // public Card card;   
    public DeckScript deckScript;
    public GameObject[] hand; // Array of card objects on the table
    public int handValue = 0; // Total value of participant's hand
    public Text scoreText;
    public bool isBusted = false;

    [SerializeField] private VisualDeck visualDeck;
    
    protected int cardIndex = 0; // Index of the next card to be turned over
    protected List<Card> aceList = new List<Card>(); // Tracking aces for 1 to 11 conversions
    private static bool m_InGetCard = false;

    public virtual IEnumerator PlayTurn()
    {
        while (handValue < 17)
            yield return GetCard();
    }
    
    public virtual IEnumerator StartHand()
    {
        yield return GetCard();
        yield return GetCard();
    }

    public void ResetHand()
    {
        for (int i = 0; i < hand.Length; i++)
        {
            hand[i].GetComponent<Card>().ResetCard();
            hand[i].SetActive(false);
        }

        isBusted = false;
        cardIndex = 0;
        handValue = 0;
        aceList = new List<Card>();
        scoreText.text = "Hand: " + handValue;
    }

    public int GetCardIndex()
    {
        return cardIndex;
    }
    
    protected IEnumerator GetCard()
    {
        yield return AnimWrapper();
        yield return MyGetCard();
    }

    private IEnumerator AnimWrapper()
    {
        yield return visualDeck.GetCardAnim(hand[cardIndex].transform.position);
    }
    
    private IEnumerator MyGetCard()
    {
        int cardValue = deckScript.DealCard(hand[cardIndex].GetComponent<Card>());
        hand[cardIndex].SetActive(true);
        handValue += cardValue;

        if (cardValue == 1)
        {
            aceList.Add(hand[cardIndex].GetComponent<Card>());
        }

        AceCheck();
        cardIndex++;
        scoreText.text = "Hand: " + handValue;
        isBusted = handValue > 21;
        yield return null;
    }
    
    private void AceCheck()
    {
        foreach (Card ace in aceList)
        {
            if (handValue + 10 < 22 && ace.GetValueOfCard() == 1)
            {
                ace.SetValue(11);
                handValue += 10;
            }
            else if (handValue > 21 && ace.GetValueOfCard() == 11)
            {
                ace.SetValue(1);
                handValue -= 10;
            }
        }
    }

    public int GetFirstCardValue()
    {
        return hand[0].GetComponent<Card>().GetValueOfCard();
    }
}