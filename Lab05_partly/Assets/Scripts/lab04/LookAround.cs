using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class LookAround : MonoBehaviour
{
    // ruch wokó³ osi Y bêdzie wykonywany na obiekcie gracza, wiêc
    // potrzebna nam referencja do niego (konkretnie jego komponentu Transform)
    public Transform player;

    public float sensitivity = 200f;

    void Start()
    {
        // zablokowanie kursora na œrodku ekranu, oraz ukrycie kursora
        Cursor.lockState = CursorLockMode.Locked;
    }

    // Update is called once per frame
    void Update()
    {
        // pobieramy wartoœci dla obu osi ruchu myszy
        float mouseXMove = Input.GetAxis("Mouse X") * sensitivity * Time.deltaTime;
        float mouseYMove = Input.GetAxis("Mouse Y") * sensitivity * Time.deltaTime;

        player.Rotate(Vector3.up * mouseXMove);

        // ograniczenie obracania kamery do -90 i +90 stopni góra-dó³
        float currentXRotation = transform.localEulerAngles.x;
        float clampedXRotation = Mathf.Clamp(currentXRotation, -90f, 90f);
        transform.localEulerAngles = new Vector3(clampedXRotation, transform.localEulerAngles.y, transform.localEulerAngles.z);
    }
}