using System.Collections;
using System.Collections.Generic;
using System.Diagnostics;
using UnityEngine;

using Vector3 = UnityEngine.Vector3;
using Debug = UnityEngine.Debug;


public class DoorController : MonoBehaviour
{
    private bool isMoving = false;
    private bool moveToTarget = true;
    public Transform targetLocat;
    public float speed = 1.0f;
    private Vector3 startPosition;
    private Vector3 endPosition;


    void Start()
    {
        startPosition = transform.position;
        if (targetLocat != null)
        {
            endPosition = targetLocat.position;
        }
    }

    void Update()
    {
        if (isMoving)
        {
            MovePlatform();
        }
    }
    void MovePlatform()
    {
        Vector3 newPosition = moveToTarget ? endPosition : startPosition;
        transform.position = Vector3.MoveTowards(transform.position, newPosition, speed * Time.deltaTime);

        if (transform.position == newPosition)
        {

            isMoving = false;

        }
    }
    private void OnTriggerEnter(Collider coll)
    {
        Debug.Log("Gracz jest przed drzwiami");
        Debug.Log("Compare tag" + coll.CompareTag("Player"));
        Debug.Log("Poruszanie " + isMoving);

        if (coll.CompareTag("Player") && !isMoving)
        {
            Debug.Log("Drzwi się otwierają");
            isMoving = true;
            moveToTarget = true;
        }
    }
}
