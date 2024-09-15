using System.Collections;
using UnityEngine;

public class Dealer : Participant
{
    [SerializeField] private GameObject hideCard;

    public override IEnumerator PlayTurn()
    {
        while (handValue < 17)
        {
            yield return GetCard();
        }
    }
    
    public override IEnumerator StartHand()
    {
        yield return GetCard();
        hideCard.SetActive(true);
        yield return GetCard();
    }
}