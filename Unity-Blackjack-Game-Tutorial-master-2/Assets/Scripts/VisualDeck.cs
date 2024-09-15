using System.Collections;
using UnityEngine;

public class VisualDeck : MonoBehaviour
{
    [SerializeField] private float m_DurationOfAnim = 1.0f;
    [SerializeField] private float m_SecondsBetweenAnims = 0.1f;

    private Vector2 originalPosition;

    private void Start()
    {
        originalPosition = transform.position;
    }
    
    public IEnumerator GetCardAnim(Vector2 cardPosition)
    {
        float timeElapsed = 0;
        while (timeElapsed < m_DurationOfAnim)
        {
            transform.position = Vector2.Lerp(originalPosition, cardPosition, timeElapsed / m_DurationOfAnim);
            timeElapsed += Time.deltaTime;
            yield return null;
        }
        yield return new WaitForSeconds(m_SecondsBetweenAnims);
    }
}
