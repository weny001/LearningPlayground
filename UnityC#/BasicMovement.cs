﻿using System.Collections;
using System.Collections.Generic;
using UnityEngine;
//BasicMovement must be the script name otherwise wont compile
public class BasicMovement : MonoBehaviour 
{
    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update() {

        Vector3 horizontal = new Vector3(Input.GetAxis("Horizontal"), 0.0f, 0.0f);
        transform.position = transform.position + horizontal * Time.deltaTime;
        
    }
}
