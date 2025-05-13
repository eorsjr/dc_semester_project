import os
import pickle
from dc_semester_project.utils import LZ77, LZ78, Huffman

def decompress_file(compressed_path: str, output_path: str, algorithm: str):
    """
    Decompress a file using the specified algorithm.
    Parameters
    ----------
    compressed_path : str
        The path to the compressed file to be decompressed.
    output_path : str
        The path to save the decompressed file. If None, the decompressed file will be saved with the same name as the compressed file with an appropriate extension.
    algorithm : str
        The decompression algorithm to use. Options are "lz77", "lz78", or "huffman".
    Returns
    -------
    str
        The path to the decompressed file.
    Raises
    ------
    FileNotFoundError
        If the compressed file does not exist.
    ValueError
        If the specified algorithm is not supported or cannot be inferred from the file extension.
    """
    if not os.path.exists(compressed_path):
        raise FileNotFoundError(f"File not found: {compressed_path}")

    if algorithm == "lz77":
        decompressor = LZ77()
    elif algorithm == "lz78":
        decompressor = LZ78()
    elif algorithm == "huffman":
        decompressor = Huffman()
    else:
        raise ValueError(f"Unsupported algorithm: {algorithm}")

    # Load the compressed data
    with open(compressed_path, "rb") as f:
        compressed_data = pickle.load(f)

    # Decompress the data
    decompressed_data = decompressor.decompress(compressed_data)

    # Save the decompressed data
    with open(output_path, "wb") as f:
        f.write(decompressed_data)

    print(f"File decompressed and saved to: {output_path}")
    return output_path