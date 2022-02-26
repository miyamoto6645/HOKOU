using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PlayerController : MonoBehaviour
{
    Rigidbody2D rbody; //Rigidbody2D�^�̕ϐ�
    float axisH = 0.0f; //����

    // Start is called before the first frame update
    void Start()
    {
        //Rigidbody2D������Ă���
        rbody = this.GetComponent<Rigidbody2D>();
       
    }

    // Update is called once per frame
    void Update()
    {
        //���������̓��͂��`�F�b�N
        axisH = Input.GetAxisRaw("Horizontal");
    }

    void FixedUpdate()
    {
    //���x���X�V
    rbody.velocity = new Vector2(axisH * 3.0f, rbody.velocity.y);
    }
}
