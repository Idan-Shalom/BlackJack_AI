using System.Collections;

public class BasicPlayer : Player
{
    public override IEnumerator PlayTurn()
    {
        while (!isBusted && handValue < 21)
        {
            var action = getBasicAction();
                
            if (action == 0) // Stand
                break;
            else // Hit
                yield return GetCard();
        }
    }
        

    private int getBasicAction()
    {
        int dealerrCard = dealerCard;
        if (handValue <= 11) return 1; //hit
        if (handValue == 12)
        {
            if (dealerrCard <= 3|| dealerrCard >= 7) return 1; //hit
            return 0;
        }
        bool hasUsableAce = aceList.Exists(c => c.GetValueOfCard() == 11) && handValue <= 21;
        if (hasUsableAce)//soft
        {
            if (handValue <= 17) return 1; //hit
            if (dealerrCard <= 8) return 0;
            return 1;
        }
        if (handValue <= 16)
        {
            if (dealerrCard <= 6) return 0;
            return 1;
        }
        return 0;
    }

}