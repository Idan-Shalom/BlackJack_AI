using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class GameManager : MonoBehaviour
{
    [Header("SimulationParams")] 
    [SerializeField] private int amountOfGamesToRun = 1000;
    [SerializeField] private float m_DelayBetweenGames = 0.0001f;
    
    [Header("Dealer and players' scripts")]
    public Dealer dealerScript;
    public List<Player> aiPlayers;

    [Header("public text to access and update - HUD")]
    public Text mainText;
    
    [Header("Card hiding dealer's 2nd card")]
    public GameObject hideCard;
    
    private int pot = 20; // How much is bet
    private int dealerStart;
    private int gamesPlayedSoFar = 0;
    private DeckScript deck;
    private Dictionary<Player, int> playerToWinsDictionary;
    private Dictionary<Player, Text> playerToTextDictionary;
    
    [Header("Automated game stats")] 
    public Text[] playersWinsTexts;
    
    private void Start()
    {
        deck = GameObject.Find("Deck").GetComponent<DeckScript>();
        
        // setup all dictionaries
        playerToWinsDictionary = new Dictionary<Player, int>();
        playerToTextDictionary = new Dictionary<Player, Text>();
        foreach (var aiPlayer in aiPlayers) playerToWinsDictionary.Add(aiPlayer, 0);
        for (int i = 0; i < aiPlayers.Count; i++) playerToTextDictionary.Add(aiPlayers[i], playersWinsTexts[i]);
        
        // setup all player wins texts
        foreach (var pair in playerToTextDictionary) pair.Value.text = pair.Key.name + " wins: " + playerToWinsDictionary[pair.Key];
        
        StartCoroutine(InitStart());
    }

    private IEnumerator InitStart()
    {
        yield return new WaitForSeconds(1f);
        mainText.gameObject.SetActive(true);
        StartCoroutine(RunGameXTimes(amountOfGamesToRun));
    }
    
    private IEnumerator RunGameXTimes(int times)
    {
        for (int i = 0; i < times; i++)
        {
            yield return RunGame();
            yield return new WaitForSeconds(m_DelayBetweenGames);
        }
    }
    
    private IEnumerator StartRound()
    {
        ResetAllHands();
        foreach (Player player in aiPlayers) player.AdjustMoneyBy(-pot);
        deck.Shuffle();
        yield return StartAllHands();
    }

    private IEnumerator StartAllHands()
    {
        yield return dealerScript.StartHand();
        dealerStart = dealerScript.GetFirstCardValue();
        
        foreach (var ai in aiPlayers)
        {
            ai.LearnFirstDealerCard(dealerStart);
            yield return ai.StartHand();
        }
    }

    private void ResetAllHands()
    {
        dealerScript.ResetHand();
        foreach (var ai in aiPlayers)
            ai.ResetHand();
    }
    
    private IEnumerator RunGame()
    {
        yield return StartRound(); 
        yield return HitAIPlayers();
        yield return HitDealer();
        // yield return new WaitForSeconds(0.2f);
        yield return RoundOver();
    }

    private IEnumerator HitAIPlayers()
    {
        foreach (var ai in aiPlayers)
            yield return ai.PlayTurn();
    }

    private IEnumerator HitDealer()
    {
        yield return dealerScript.PlayTurn();
        // yield return new WaitForSeconds(0.1f);
    }

    private IEnumerator RoundOver()
    {
        foreach (var ai in aiPlayers) 
            EvaluatePlayer(ai, ai.isBusted, dealerScript.isBusted);
        foreach (var pair in playerToTextDictionary)
        {
            var percentage = ((float)playerToWinsDictionary[pair.Key] / gamesPlayedSoFar) * 100f; 
            pair.Value.text = pair.Key.name + " win percentage: " + percentage + "%";
        }
        gamesPlayedSoFar++;
        mainText.text = "Games played:\n" + gamesPlayedSoFar;
        
        hideCard.SetActive(false);
        // yield return new WaitForSeconds(0.2f);
        yield return null;
    }

    private void EvaluatePlayer(Player currentPlayer, bool playerBust, bool dealerBust)
    {
        // Dealer wins
        if (playerBust || (!dealerBust && dealerScript.handValue > currentPlayer.handValue)) {}
        // Player wins
        else if (dealerBust || currentPlayer.handValue > dealerScript.handValue)
        {
            if (currentPlayer.handValue == 21)
            {
                currentPlayer.AdjustMoneyBy((int)(pot * 2.5f));
                playerToWinsDictionary[currentPlayer]++;
                return;
            }
            
            playerToWinsDictionary[currentPlayer]++;
            currentPlayer.AdjustMoneyBy(pot * 2);
        }
        // Tie
        else if (currentPlayer.handValue == dealerScript.handValue)
        {
            currentPlayer.AdjustMoneyBy(pot);
        }
        else
        {
            print("Shouldn't get here!");
        }
    }
}
