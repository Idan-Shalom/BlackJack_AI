using UnityEngine;

public class DeckScript : MonoBehaviour
{
    public Sprite[] cardSprites;
    public Sprite cardBackSprite;
    private int[] cardValues = new int[52];
    private int currentIndex = 0;

    private void Start()
    {
        GetCardValues();
    }

    private void GetCardValues()
    {
        int num;
        // Loop to assign values to the cards
        for (int i = 0; i < cardSprites.Length; i++)
        {
            num = (i + 1) % 13;
            // if there is a remainder after x/13, then remainder
            // is used as the value, unless over 10, the use 10
            if(num > 10 || num == 0)
            {
                num = 10;
            }
            cardValues[i] = num++;
        }
    }

    public void Shuffle()
    {
        for (int i = cardSprites.Length - 1; i > 0; --i)
        {
            int j = Random.Range(0, i + 1); // Correct random index calculation
            (cardSprites[i], cardSprites[j]) = (cardSprites[j], cardSprites[i]);
            (cardValues[i], cardValues[j]) = (cardValues[j], cardValues[i]);
        }
        currentIndex = 1;
    }
    
    public int DealCard(Card card)
    {
        currentIndex = Random.Range(0, cardSprites.Length);
        card.SetSprite(cardSprites[currentIndex]);
        card.SetValue(cardValues[currentIndex]);
        return card.GetValueOfCard();
    }

    public Sprite GetCardBack()
    {
        return cardBackSprite;
    }
}
