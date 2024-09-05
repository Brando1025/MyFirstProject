import cv2
import numpy as np


def main():
    # 读取输入图像（假设为二值图像）
    image = cv2.imread("assets/test.jpg", cv2.IMREAD_GRAYSCALE)

    # 确保图像是二值图像
    _, binary = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

    # 查找连通区域
    num_labels, labels = cv2.connectedComponents(binary)

    # 创建一个随机颜色的图像来显示连通区域
    output = np.zeros((image.shape[0], image.shape[1], 3), dtype=np.uint8)

    # 为每个连通区域着色
    for i in range(1, num_labels):  # 从1开始，因为0是背景
        mask = labels == i
        output[mask] = np.random.randint(0, 255, size=3, dtype=np.uint8)

    # 显示结果
    cv2.imshow("Connected Components", output)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # 保存结果
    cv2.imwrite("output.png", output)


if __name__ == "__main__":
    main()
