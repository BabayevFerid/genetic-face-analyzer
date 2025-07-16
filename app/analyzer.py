from deepface import DeepFace

def analyze_image(image_path):
    try:
        result = DeepFace.analyze(
            img_path=image_path,
            actions=['age', 'gender', 'emotion', 'race'],
            enforce_detection=False
        )
        return result[0]  # First face result
    except Exception as e:
        print("Analysis error:", e)
        return None
