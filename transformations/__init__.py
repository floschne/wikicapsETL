from loguru import logger

from .compression_transformation import CompressionTransformation
from .image_transformation_base import ImageTransformationBase
from .resize_transformation import ResizeTransformation


def create_image_transformations_from_config(config):
    transformations = []

    try:
        for t in config.transformation.image:
            name = list(t.keys())[0]
            if "resize" == name.lower():
                maxWidth = t[name].maxWidth
                maxHeight = t[name].maxHeight
                resampling = t[name].resampling
                transformations.append(ResizeTransformation(maxWidth, maxHeight, resampling))
            elif "compress" == name.lower():
                optimize = t[name].optimize
                dpi = (t[name].dpi, t[name].dpi)
                transformations.append(CompressionTransformation(optimize, dpi))
            else:
                raise ValueError(f"Cannot parse Transformation '{name}'!")
        return transformations
    except ValueError:
        logger.exception("Cannot parse Transformation Config!")
