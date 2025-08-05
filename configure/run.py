import json, os

python_version_dict = {
    "SimpleHTR": "3.6",
    "StyleGAN-Tensorflow": "3.6",
    "cnn_captcha": "3.6",
    "deep-belief-network": "3.6",
    "crnn.pytorch": "3.7",
    "siren": "3.7",
    "Deep-SAD-PyTorch": "3.7",
    "PyTorch-ENet": "3.7",
    "ConSinGAN": "3.5",
    "spert": "3.7",
    "hifi-gan": "3.7",
    "DexiNed": "3.7",
    "KiU-Net-pytorch": "3.6",
    "Sentence-VAE": "3.7",
    "MASTER-pytorch": "3.6",
    "nlp_classification": "3.7",
    "pytorch-hed": "3.7",
    "3d-ken-burns": "3.7",
    "sepconv-slomo": "3.7",
    "svoice": "3.7",
    "LaneATT": "3.8",
    "JointBERT": "3.6",
    "pytorch-liteflownet": "3.7",
    "R-BERT": "3.7",
    "pytorch-spynet": "3.7",
    "GLCIC-PyTorch": "3.7",
    "DeepMosaics": "3.7",
    "PedalNetRT": "3.7",
    "BERT-NER": "3.7",
    "Federated-Learning-PyTorch": "3.7",
    "RetinaFace_Pytorch": "3.7",
    "Bert-Multi-Label-Text-Classification": "3.7",
    "siamese-pytorch": "3.7",
    "graphSAGE-pytorch": "3.6",
    "pt.darts": "3.7"
}
start = {
  "SimpleHTR": {"tensorflow": "2.4.0"},
  "StyleGAN-Tensorflow": {"tensorflow": "1.13.1", "numpy": "1.16.4"},
  "cnn_captcha": {"tensorflow": "1.7.0", "numpy": "1.16.2"},
  "deep-belief-network": {"tensorflow": "1.5.0", "numpy": "1.16.4", "scipy": "0.18.1", "scikit-learn": "0.18.1"},
  "crnn.pytorch": {"torch": "1.2.0", "torchvision": "0.4.0"},
  "siren": {"torch": "1.4.0", "numpy": "1.17.2", "matplotlib": "3.0.3"},
  "Deep-SAD-PyTorch": {"torch": "1.1.0", "torchvision": "0.3.0", "matplotlib": "3.1.0", "pillow": "6.0.0", "numpy": "1.16.4"},
  "PyTorch-ENet": {"torch": "1.1.0", "torchvision": "0.3.0", "matplotlib": "3.0.2", "pillow": "6.2.0", "numpy": "1.16.0"},
  "ConSinGAN": {"torch": "1.1.0", "torchvision": "0.2.2"},
  "spert": {"torch": "1.4.0", "numpy": "1.17.4"},
  "hifi-gan": {"torch": "1.4.0", "numpy": "1.17.4", "scipy": "1.4.1", "matplotlib": "3.1.3", "librosa": "0.7.2"},
  "DexiNed": {"opencv-python": "4.6.0.66"},
  "KiU-Net-pytorch": {"torch": "1.4.0"},
  "Sentence-VAE": {"torch": "1.5.0", "numpy": "1.18.5", "nltk": "3.6.5", "tensorboardx": "2.0"},
  "MASTER-pytorch": {"torch": "1.5.1", "torchvision": "0.6.1", "numpy": "1.16.4", "pillow": "7.2.0"},
  "nlp_classification": {"torch": "1.5.0", "pandas": "1.0.3"},
  "pytorch-hed": {"torch": "1.7.0", "numpy": "1.15.0", "pillow": "5.0.0"},
  "3d-ken-burns": {"torch": "1.7.0", "torchvision": "0.8.0"},
  "sepconv-slomo": {"torch": "1.7.0", "pillow": "9.3.0"},
  "svoice": {"torch": "1.6.0", "torchaudio": "0.6.0", "pesq": "0.0.2"},
  "LaneATT": {"scipy": "1.4.1", "scikit-learn": "0.23.2"},
  "JointBERT": {"torch": "1.6.0", "seqeval": "0.0.12"},
  "pytorch-liteflownet": {"torch": "1.6.0", "pillow": "9.3.0"},
  "R-BERT": {"torch": "1.6.0"},
  "pytorch-spynet": {"torch": "1.6.0", "numpy": "1.15.0"},
  "GLCIC-PyTorch": {"torch": "1.9.0", "torchvision": "0.10.0", "opencv-python": "4.5.2.54", "numpy": "1.19.2", "pillow": "8.2.0", "tqdm": "4.61.1"},
  "DeepMosaics": {"torch": "1.7.1", "torchvision": "0.8.2", "numpy": "1.19.3", "opencv-python": "4.5.1.48", "tensorboardx": "2.2"},
  "PedalNetRT": {"torch": "1.7.0", "scipy": "1.5.4", "numpy": "1.19.4", "pytorch-lightning": "1.1.0"},
  "BERT-NER": {"torch": "1.2.0", "seqeval": "0.0.5", "tqdm": "4.31.1"},
  "Federated-Learning-PyTorch": {"torch": "1.2.0", "torchvision": "0.4.0", "numpy": "1.15.4", "matplotlib": "3.0.1"},
  "RetinaFace_Pytorch": {"torch": "1.1.0", "torchvision": "0.3.0", "numpy": "1.16.4", "scikit-image": "0.15.0", "pillow": "6.1.0", "tensorboardx": "1.8"},
  "Bert-Multi-Label-Text-Classification": {"torch": "1.3.0", "numpy": "1.17.2", "transformers": "2.5.1", "matplotlib": "3.1.1"},
  "siamese-pytorch": {"torch": "1.0.1", "torchvision": "0.2.1", "numpy": "1.16.1", "pillow": "5.4.1"},
  "graphSAGE-pytorch": {"torch": "1.0.1", "numpy": "1.16.2", "scikit-learn": "0.20.3"},
  "pt.darts": {"torch": "1.0.0", "torchvision": "0.2.1", "tensorboardx": "1.6"}
}


knowledge_path = "/dataset/lei/" # Change to your directory
proj_path = "/dataset/lei/projects/" # Change to your directory
requirements_path = "/dataset/lei/requirements/" # Change to your directory
if __name__ == "__main__":
    with open("./test.json") as f:
        data = json.load(f)
    for proj in data:
        for lib in data[proj]:
            for version in data[proj][lib]:
                if not os.path.exists(f"./{proj}/{lib}/{version}"):
                    os.makedirs(f"./{proj}/{lib}/{version}")
                with open(f"./{proj}/{lib}/{version}/config.json", 'w') as f:
                    json.dump({
                        "projPath": f"{proj_path}{proj}",
                        "requirementsPath": f"{requirements_path}{proj}/requirements.txt",
                        "targetLibrary": f"{lib}",
                        "startVersion": f"{start[proj][lib]}",
                        "targetVersion": f"{version}",
                        "pythonVersion": f"{python_version_dict[proj]}",
                        "knowledgePath": knowledge_path
                    }, f, indent=7)
                