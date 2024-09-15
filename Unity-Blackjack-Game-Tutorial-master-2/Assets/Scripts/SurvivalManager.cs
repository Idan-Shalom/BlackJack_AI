using System.Collections;
using System.Collections.Generic;
using System.IO;
using UnityEngine;
using UnityEngine.UI;
public class SurvivalManager : MonoBehaviour
{
    [Header("SimulationParams")]
    [SerializeField] private float m_DelayBetweenGames = 0.0001f;
    
    [Header("Dealer and players' scripts")]
    public Dealer dealerScript;
    public List<Player> aiPlayers;
    
    [Header("public text to access and update - HUD")]
    public Text mainText;
    
    [Header("Card hiding dealer's 2nd card")]
    public GameObject hideCard;
    private int pot = 10; // How much is bet
    private int dealerStart;
    private int gamesPlayedSoFar = 0;
    private DeckScript deck;
    private Dictionary<Player, int> playerToWinsDictionary;
    private Dictionary<Player, Text> playerToTextDictionary;
    private string totalString;  
    
    [Header("Automated game stats")]
    public Text[] playersWinsTexts;
    
    private void Start()
    {
        deck = GameObject.Find("Deck").GetComponent<DeckScript>();

        // Setup all dictionaries
        playerToWinsDictionary = new Dictionary<Player, int>();
        playerToTextDictionary = new Dictionary<Player, Text>();
        foreach (var aiPlayer in aiPlayers)
        {
            playerToWinsDictionary.Add(aiPlayer, 0);
        }
        for (int i = 0; i < aiPlayers.Count; i++)
        {
            playerToTextDictionary.Add(aiPlayers[i], playersWinsTexts[i]);
        }
        // Setup all player wins texts
        foreach (var pair in playerToTextDictionary)
        {
            pair.Value.text = pair.Key.name + " wins: " + playerToWinsDictionary[pair.Key];
        }
        StartCoroutine(InitStart());
    }
    private IEnumerator InitStart()
    {
        yield return new WaitForSeconds(2f);
        mainText.gameObject.SetActive(true);
        StartCoroutine(RunSurvivalGame());
    }
    private IEnumerator RunSurvivalGame()
    {
        while (AtleastOneSurvives())
        {
            yield return RunGame();
            yield return new WaitForSeconds(m_DelayBetweenGames);
        }
        File.WriteAllText("r.txt", totalString);
    }
    private bool AtleastOneSurvives()
    {
        foreach(var player in aiPlayers)
        {
            if (player.GetMoney() > 0) return true;
        }

        return false;
        // return aiPlayers[0] != null && aiPlayers[0].GetMoney() > 0 ||
        //        aiPlayers[1] != null && aiPlayers[1].GetMoney() > 0 ||
        //        aiPlayers[2] != null && aiPlayers[2].GetMoney() > 0;
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
        yield return RoundOver();
        for (int i = 0; i < aiPlayers.Count; i++)
        {
            if (aiPlayers[i].GetMoney() <= 0)
            {
                print(aiPlayers[i].name + " survived " + gamesPlayedSoFar + " games");
                aiPlayers.RemoveAt(i);
            }
        }
    }
    private IEnumerator HitAIPlayers()
    {
        foreach (var ai in aiPlayers)
            yield return ai.PlayTurn();
    }
    private IEnumerator HitDealer()
    {
        yield return dealerScript.PlayTurn();
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
        // Log the money of each player at the end of each round
        LogPlayerMoney();
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

    private void LogPlayerMoney()
    {
        totalString += "\n" + aiPlayers[0].GetMoney();
    }
}