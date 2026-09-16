import cv2
import numpy as np

class ShapeDetector:
    def __init__(self, video_path):
        self.cap = cv2.VideoCapture(video_path)

    def process_frame(self, frame):
        frame = cv2.medianBlur(frame, 5)
        blurred = cv2.GaussianBlur(frame, (5, 5), 0)
        hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
        #blue mask
        lower_blue = np.array([100, 150, 0])
        upper_blue = np.array([140, 255, 255])
        blue_mask = cv2.inRange(hsv, lower_blue, upper_blue)
        #red mask
        lower_red1 = np.array([0, 150, 70])
        upper_red1 = np.array([10, 255, 255])
        lower_red2 = np.array([170, 150, 70])
        upper_red2 = np.array([180, 255, 255])
        red_mask = cv2.inRange(hsv, lower_red1, upper_red1) + cv2.inRange(hsv, lower_red2, upper_red2)
        
        self.detect_and_draw(frame, blue_mask, "Blue Square", (255, 0, 0))
        self.detect_and_draw(frame, red_mask, "Red Circle", (0, 0, 255))
        
        return frame

    def detect_and_draw(self, frame, mask, label, color):
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        for cnt in contours:
            area = cv2.contourArea(cnt)
            if area > 100: 
                peri = cv2.arcLength(cnt, True)
                approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
                
                if len(approx) == 4 and label == "Blue Square":
                    cv2.drawContours(frame, [approx], -1, color, 3)
                    x, y, w, h = cv2.boundingRect(approx)
                    cv2.putText(frame, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
                
                elif len(approx) > 4 and label == "Red Circle":
                    cv2.drawContours(frame, [cnt], -1, color, 3)
                    x, y, w, h = cv2.boundingRect(cnt)
                    cv2.putText(frame, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

    def run(self):
        while self.cap.isOpened():
            ret, frame = self.cap.read()
            if not ret:
                break
            
            processed_frame = self.process_frame(frame)
            cv2.imshow('Subtask 2 - Shape Detection', processed_frame)
            #press q to exit 
            if cv2.waitKey(30) & 0xFF == ord('q'):
                break
                
        self.cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    video_path = 'thrown_shapes_noisy_30s.mp4' 
    detector = ShapeDetector(video_path)
    detector.run()