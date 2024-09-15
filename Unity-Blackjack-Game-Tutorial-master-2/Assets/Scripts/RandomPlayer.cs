using System;
using System.Collections;

public class RandomPlayer : Player
{
    private Random random = new Random();
    
    public override IEnumerator PlayTurn()
    {
        while (handValue < 21)
        {
            int x = random.Next(0, 2);
            if (x == 0)
                yield return GetCard();
            else
                yield break;
        }
    }
}