from qanet import Graph
import tensorflow as tf

if __name__ == '__main__': 
    g = Graph("train")
    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        print g.x_w_emb.shape
        print g.q_emb.shape        
        print g.x_c_emb.shape
        print g.x_emb.shape
