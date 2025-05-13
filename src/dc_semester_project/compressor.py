import os
import pickle
from dc_semester_project.utils import LZ77, LZ78, Huffman

def compress_file(input_path: str, output_path: str, algorithm: str, **kwargs):
    """ 
    Compress a file using the specified algorithm.
    Parameters
    ----------
    input_path : str
        The path to the input file to be compressed.
    output_path : str
        The path to save the compressed file. If None, the compressed file will be saved with the same name as the input file with an appropriate extension.
    algorithm : str
        The compression algorithm to use. Options are "lz77", "lz78", or "huffman".
    **kwargs : dict
        Additional arguments to pass to the compression algorithm.
    Returns
    -------
    str
        The path to the compressed file.
    Raises
    ------
    FileNotFoundError
        If the input file does not exist.
    ValueError
        If the specified algorithm is not supported.
    """
    if not os.path.exists(input_path):
            raise FileNotFoundError(f"File not found: {input_path}")
    
    with open(input_path, 'rb') as f:
        data = f.read()
        
    algorithm = algorithm.lower()
    
    if algorithm == "lz77":
        compressor = LZ77(**kwargs)
        compressed_data = compressor.compress(data)
        extension = ".lz77"
    elif algorithm == "lz78":
        compressor = LZ78(**kwargs)
        compressed_data = compressor.compress(data)
        extension = ".lz78"
    elif algorithm == "huffman":
        compressor = Huffman(**kwargs)
        compressed_data = compressor.compress(data)
        extension = ".huffman"
    else:
        raise ValueError(f"Unsupported algorithm: {algorithm}")
    
    if output_path is None:
        output_path = f"{input_path}{extension}"
    elif not output_path.endswith(extension):
        output_path += extension


    with open(output_path, "wb") as f:
        pickle.dump(compressed_data, f)

    print(f"File compressed and saved to: {output_path}")
    return output_path