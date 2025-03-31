import argparse
import os
from trex import TRex2APIWrapper, visualize
from PIL import Image
import numpy as np


def get_args():
    parser = argparse.ArgumentParser(description="Interactive Inference")
    parser.add_argument(
        "--token",
        type=str,
        help="The token for T-Rex2 API. We are now opening free API access to T-Rex2",
    )
    parser.add_argument(
        "--box_threshold", type=float, default=0.3, help="The threshold for box score"
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = get_args()
    trex2 = TRex2APIWrapper(args.token)
    prompts = [
        {
            "prompt_image": "images/Pic_1.jpg",
            "rects": [[985, 515, 49.12, 37.51], [548, 462, 48.04, 48.17], [807, 552, 39.59, 54.19], [425, 730, 43.18, 45.74], [1205, 623, 49.47, 29.68], [1143, 662, 32.37, 44.69], [658, 870, 41.63, 52.66], [1165, 790, 38.74, 48.75], [1223, 695, 44.59, 37.92], [1035, 867, 49.34, 36.25], [667, 415, 38.17, 53.83], [1093, 572, 32.73, 41.12], [1103, 623, 41.04, 36.37], [785, 835, 47.06, 45.89]],
        },
        {
            "prompt_image": "images/Pic_2.jpg",
            "rects": [[1750, 892, 61.72, 48.13], [848, 1013, 52.14, 50.16], [360, 463, 33.31, 57.27], [717, 262, 54.71, 50.04], [708, 1696, 46.2, 70.92], [1658, 704, 56.45, 40.27], [1410, 322, 55.12, 37.5]],
        },
        {
            "prompt_image": "images/Pic_2.jpg",
            "rects": [[1750, 892, 61.72, 48.13], [848, 1013, 52.14, 50.16], [360, 463, 33.31, 57.27], [717, 262, 54.71, 50.04], [708, 1696, 46.2, 70.92], [1658, 704, 56.45, 40.27], [1410, 322, 55.12, 37.5]],
        },
    ]
    embedding_url = trex2.customize_embedding(prompts)
    print(f"Customized embedding URL: {embedding_url}")
