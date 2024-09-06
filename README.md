## Overview

This project focuses on building a Convolutional Neural Network (CNN) to classify images of cats and dogs. The goal is to develop a model that can accurately identify whether an image contains a cat or a dog.


## Dataset

The dataset used for this project consists of labeled images of cats and dogs. The images are divided into training and testing sets. You can download the dataset from the following source:

- [Kaggle: Dogs vs. Cats](https://www.kaggle.com/c/dogs-vs-cats/data)

## How to Run

### Prerequisites

- Python 3.x
- Docker (optional, for containerized deployment)

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/raish123/cnnClassifier.git
    cd cnnClassifier
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the project:

    ```bash
    python main.py
    ```

### Using Docker

If you prefer using Docker, you can build and run the project in a Docker container:

1. Build the Docker image:

    ```bash
    docker build -t cnn-classifier .
    ```

2. Run the Docker container:

    ```bash
    docker run -p 8080:8080 cnn-classifier
    ```

## Model Architecture

The Convolutional Neural Network (CNN) used in this project consists of the following layers:

- **Convolutional Layer:** Extracts features from the input images.
- **Pooling Layer:** Reduces the spatial dimensions of the feature maps.
- **Fully Connected Layer:** Maps the extracted features to the output classes (cat and dog).

## Training and Evaluation

- **Training:** The model is trained on the training dataset, which contains labeled images of cats and dogs.
- **Evaluation:** The model's performance is evaluated using the testing dataset. Metrics such as accuracy, precision, recall, and F1-score are used to assess the model.

## Results

The final model achieves an accuracy of `XX%` on the testing dataset. Here are some sample predictions:

| Image        | Predicted Label | Actual Label |
|--------------|-----------------|--------------|
| ![Cat Image](images/cat_sample.png) | Cat             | Cat          |
| ![Dog Image](images/dog_sample.png) | Dog             | Dog          |

## Conclusion

This project demonstrates the effectiveness of CNNs in image classification tasks, particularly in distinguishing between cats and dogs. Further improvements could include data augmentation, hyperparameter tuning, and experimentation with different CNN architectures.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Kaggle: Dogs vs. Cats Dataset](https://www.kaggle.com/c/dogs-vs-cats/data)
- [TensorFlow](https://www.tensorflow.org/) - The deep learning framework used in this project.

