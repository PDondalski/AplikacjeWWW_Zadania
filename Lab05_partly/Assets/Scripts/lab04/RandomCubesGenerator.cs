using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class RandomCubesGenerator : MonoBehaviour
{
    private List<Vector3> positions = new List<Vector3>();
    [SerializeField]
    private float delay = 3.0f;
    [SerializeField]
    private GameObject block;
    [SerializeField]
    private int objectsAmount = 10;
    [SerializeField]
    private Material[] materials;

    private Bounds bounds;

    void Start()
    {
        Renderer renderer = GetComponent<Renderer>();
        bounds = renderer.bounds;

        for (int i = 0; i < objectsAmount; i++)
        {
            Vector3 position = new Vector3(Random.Range(bounds.min.x, bounds.max.x), 5, Random.Range(bounds.min.z, bounds.max.z));
            positions.Add(position);
        }

        // Uruchamiamy coroutine
        StartCoroutine(GenerujObiekt());
    }

    IEnumerator GenerujObiekt()
    {
        Debug.Log("Wywołano coroutine");
        foreach (Vector3 pos in positions)
        {
            int randomMaterialIndex = Random.Range(0, materials.Length);
            GameObject newBlock = Instantiate(this.block, pos, Quaternion.identity);
            newBlock.GetComponent<Renderer>().material = materials[randomMaterialIndex];
            yield return new WaitForSeconds(this.delay);
        }
    }
}