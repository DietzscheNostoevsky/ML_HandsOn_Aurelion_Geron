# MNIST Distributed Training 

I wanted to devise a strategy to take a model and simultaneously train it on two devices: 

        On Colab
        And on a Home PC


And at the end combine the results on both training to speed up the training process, while increasing the accuracy of the model. 


The directory contains 3 files : 
        1. colab_training.py
        2. home_training.py
        3. combine_results.py
   
The idea is to run the first two files simultaneously on differnt platforms, and combine the results at the end. 

Using MNIST dataset to test 