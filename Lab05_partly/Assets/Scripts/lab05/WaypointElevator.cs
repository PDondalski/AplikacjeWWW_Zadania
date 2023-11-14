using System.Collections;
using System.Collections.Generic;
using System.Diagnostics;
using UnityEngine;

using Vector3 = UnityEngine.Vector3;
using Debug = UnityEngine.Debug;


public class WaypointElevator : MonoBehaviour
{
    private bool isMoving = false;
    public Transform targetLocat;
    public float speed = 1.0f;
    private Vector3 startPosition;
    private Vector3 endPosition;
    public List<Transform> waypoints;
    private int currentWaypointIndex = 0;
    private bool isGoingForward = true;

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
        Vector3 newPosition = waypoints[currentWaypointIndex].position;
        transform.position = Vector3.MoveTowards(transform.position, newPosition, speed * Time.deltaTime);

        if (transform.position == newPosition)
        {
            if (isGoingForward)
            {
                currentWaypointIndex++;
                if (currentWaypointIndex >= waypoints.Count)
                {
                    currentWaypointIndex = waypoints.Count - 2;
                    isGoingForward = false;
                }
            }
            else
            {
                currentWaypointIndex--;
                if (currentWaypointIndex < 0)
                {
                    currentWaypointIndex = 0;
                    isGoingForward = true;
                    isMoving = false;
                }
            }
        }
    }

    private void OnTriggerEnter(Collider coll)
    {

        if (coll.CompareTag("Player") && !isMoving)
        {
            isMoving = true;
        }
    }
}
