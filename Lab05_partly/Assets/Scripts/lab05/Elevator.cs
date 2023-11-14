using System.Collections;
using System.Collections.Generic;
using System.Diagnostics;
using UnityEngine;
using Debug = UnityEngine.Debug;

public class Elevator : MonoBehaviour
{
    public float elevatorSpeed = 2f;
    public float distance = 6.6f;
    private bool isRunningRight = true;
    private bool isRunningLeft = false;
    private float leftPosition;
    private float rightPosition;
    private bool playerOnElevator = false;
    private Transform oldParent;

    void Start()
    {
        rightPosition = transform.position.x + distance;
        leftPosition = transform.position.x;
    }

    void Update()
    {
        if (playerOnElevator)
        {
            if (isRunningRight && transform.position.x >= rightPosition)
            {
                isRunningRight = false;
                isRunningLeft = true;
            }
            else if (isRunningLeft && transform.position.x <= leftPosition)
            {
                isRunningLeft = false;
                isRunningRight = true;
            }

            if (isRunningRight)
            {
                Vector3 move = transform.right * elevatorSpeed * Time.deltaTime;
                transform.Translate(move);
            }
            else if (isRunningLeft)
            {
                Vector3 move = -transform.right * elevatorSpeed * Time.deltaTime;
                transform.Translate(move);
            }
        }
    }

    private void OnTriggerEnter(Collider other)
    {
        if (other.gameObject.CompareTag("Player"))
        {
            Debug.Log("Player wszed� na wind�.");
            oldParent = other.gameObject.transform.parent;
            // skrypt przypisany do windy, ale other może być innym obiektem
            other.gameObject.transform.parent = transform;
            if (transform.position.x >= rightPosition)
            {
                isRunningLeft = true;
                isRunningRight = false;
                elevatorSpeed = -elevatorSpeed;
            }
            else if (transform.position.x <= leftPosition)
            {
                isRunningRight = true;
                isRunningLeft = false;
                elevatorSpeed = Mathf.Abs(elevatorSpeed);
            }
            playerOnElevator = true;
        }
    }

    private void OnTriggerExit(Collider other)
    {
        if (other.gameObject.CompareTag("Player"))
        {
            Debug.Log("Player zszedł z windy.");
            other.gameObject.transform.parent = null;
        }
    }
}