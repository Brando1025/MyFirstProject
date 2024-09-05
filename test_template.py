import pytest
import cv2
import numpy as np
import os
import awesome_template

# 假设测试图像路径
TEST_IMAGE_PATH = "assets/test.jpg"
OUTPUT_IMAGE_PATH = "output.png"


def test_connected_components_integration():
    # 假设这是一个集成测试，调用 awesome_template.py 中的代码
    awesome_template.main()  # 假设 awesome_template.py 有一个 main 函数


def test_image_loading():
    image = cv2.imread(TEST_IMAGE_PATH, cv2.IMREAD_GRAYSCALE)
    assert image is not None, "图像加载失败"
    assert len(image.shape) == 2, "图像不是灰度图像"


def test_thresholding():
    image = cv2.imread(TEST_IMAGE_PATH, cv2.IMREAD_GRAYSCALE)
    _, binary = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
    assert binary is not None, "二值化处理失败"
    assert np.unique(binary).tolist() == [0, 255], "二值化结果不是仅包含0和255"


def test_connected_components():
    image = cv2.imread(TEST_IMAGE_PATH, cv2.IMREAD_GRAYSCALE)
    _, binary = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
    num_labels, labels = cv2.connectedComponents(binary)
    assert num_labels > 1, "未检测到连通区域"
    assert labels.shape == image.shape, "标签图像尺寸与输入图像不一致"


def test_output_image_creation():
    image = cv2.imread(TEST_IMAGE_PATH, cv2.IMREAD_GRAYSCALE)
    _, binary = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
    num_labels, labels = cv2.connectedComponents(binary)

    output = np.zeros((image.shape[0], image.shape[1], 3), dtype=np.uint8)
    for i in range(1, num_labels):
        mask = labels == i
        output[mask] = np.random.randint(0, 255, size=3, dtype=np.uint8)

    assert output is not None, "输出图像创建失败"
    assert output.shape == (image.shape[0], image.shape[1], 3), "输出图像尺寸不正确"


def test_output_image_saving():
    image = cv2.imread(TEST_IMAGE_PATH, cv2.IMREAD_GRAYSCALE)
    _, binary = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
    num_labels, labels = cv2.connectedComponents(binary)

    output = np.zeros((image.shape[0], image.shape[1], 3), dtype=np.uint8)
    for i in range(1, num_labels):
        mask = labels == i
        output[mask] = np.random.randint(0, 255, size=3, dtype=np.uint8)

    cv2.imwrite(OUTPUT_IMAGE_PATH, output)
    assert os.path.exists(OUTPUT_IMAGE_PATH), "输出图像保存失败"
    saved_image = cv2.imread(OUTPUT_IMAGE_PATH)
    assert saved_image is not None, "无法加载保存的图像"
    assert saved_image.shape == output.shape, "保存的图像尺寸与输出图像不一致"


@pytest.fixture(scope="module", autouse=True)
def cleanup_output():
    """在测试结束后清理生成的输出文件"""
    yield
    if os.path.exists(OUTPUT_IMAGE_PATH):
        os.remove(OUTPUT_IMAGE_PATH)
