import torch
from torchvision import datasets
from torchvision import transforms
import matplotlib.pyplot as plt
from autoencoder import Autoenc

def main():
    model = Autoenc()
    model.test()

if __name__ == "__main__":
    main()
 