using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class BasicMovement : MonoBehaviour 
{
    // Start is called before the first frame update
    void Start()


void Update ()
 {
     if (Input.GetKey(KeyCode.LeftArrow))
     {
         transform.position += Vector3.left * speed * Time.deltaTime;
     }
     if (Input.GetKey(KeyCode.RightArrow))
     {
         transform.position += Vector3.right * speed * Time.deltaTime;
     }
     if (Input.GetKey(KeyCode.UpArrow))
     {
         transform.position += Vector3.up * speed * Time.deltaTime;
     }
     if (Input.GetKey(KeyCode.DownArrow))
     {
         transform.position += Vector3.down * speed * Time.deltaTime;
     }
 }
