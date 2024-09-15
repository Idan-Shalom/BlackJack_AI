using System;
using UnityEngine;
using UnityEngine.UI;

public class Card : MonoBehaviour
{
    private int value = 0;
    private Vector2 startPosition;
    private Camera cam;

    private void Awake()
    {
        cam = Camera.main;
    }

    private void Start()
    {
        startPosition = cam.ScreenToWorldPoint(transform.position);
    }

    public int GetValueOfCard()
    {
        return value;
    }

    public void SetValue(int newValue)
    {
        value = newValue;
    }

    public string GetSpriteName()
    {
        return GetComponent<Image>().sprite.name;
    }

    public void SetSprite(Sprite newSprite)
    {
        gameObject.GetComponent<Image>().sprite = newSprite;
    }

    public void ResetCard()
    {
        Sprite back = GameObject.Find("Deck").GetComponent<DeckScript>().GetCardBack();
        gameObject.GetComponent<Image>().sprite = back;
        value = 0;
    }

    public Vector2 GetCardPosition()
    {
        return new Vector2(transform.position.x, transform.position.y);
    }

    public Vector2 GetStartPosition()
    {
        return startPosition;
    }
}
