from flask import Flask, request, jsonify, send_file
import cv2

app = Flask(__name__)

@app.route('/api/generate-image', methods=['POST'])
def generate_image():
    # Generate the image using OpenCV
    img = cv2.imread('C:\Users\vkhan\Desktop\Hack_IOT\Codes\main_test2.jpg')  # Replace with your image path
    # Perform image processing or any necessary operations on 'img'
    # ...

    # Save the image temporarily
    temp_image_path = 'C:\Users\vkhan\Desktop\HTML\output'  # Replace with your desired temporary image path
    cv2.imwrite(temp_image_path, img)

    # Return the path of the temporary image
    response = {'image_path': temp_image_path}
    return jsonify(response)

@app.route('/api/get-image', methods=['GET'])
def get_image():
    # Retrieve the path of the temporary image
    temp_image_path = request.args.get('image_path')

    # Send the image file as a response
    return send_file(temp_image_path, mimetype='image/jpeg')

if __name__ == '__main__':
    app.run()
