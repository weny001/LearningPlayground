using UnityEngine;
using System.Collections;
//Script must be called playerscript
public class PlayerScript : MonoBehaviour {
    private Rigidbody2d mybody;

    public float speed;
    public float jumpPower;

    void start () {
        mybody - gameObject.GetComponent<Rigidbody2d>();
    }

    void Update () {
        float move = Input.GetAxis("Horizontal");
        mybody.velocity = new Vector2(move * speed, mybody.velocity.y);

        if(Input.GetKey(KeyCode.Space)) {
            anybody.velocity = new Vector2(mybody.velocity.x, jumpPower);
        }
    }
}
