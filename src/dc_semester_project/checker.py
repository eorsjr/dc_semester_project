import os
import math

def checker(original_path: str, decompressed_path: str):
    """
    Compare the original and decompressed files to check if they are identical.
    
    Parameters
    ----------
    original_path : str
        The path to the original file.
    decompressed_path : str
        The path to the decompressed file.
        
    Returns
    -------
    bool
        True if the files are identical, False otherwise.
        
    Raises
    ------
    FileNotFoundError
        If the original or decompressed file does not exist.
    """
    
    if not os.path.exists(original_path):
        print(f"Original file not found: {original_path}")
        return False

    if not os.path.exists(decompressed_path):
        print(f"Decompressed file not found: {decompressed_path}")
        return False

    with open(original_path, "rb") as original, open(decompressed_path, "rb") as decompressed:
        original_data = original.read()
        decompressed_data = decompressed.read()

    if original_data == decompressed_data:
        print("The original and decompressed files are identical.")
    else:
        print("The original and decompressed files are NOT identical.")

def compression_ratio(original_path: str, compressed_path: str):
    
    if not os.path.exists(original_path):
        print(f"Original file not found: {original_path}")
        return 0.0

    if not os.path.exists(compressed_path):
        print(f"Compressed file not found: {compressed_path}")
        return 0.0

    original_size = os.path.getsize(original_path)
    compressed_size = os.path.getsize(compressed_path)

    if compressed_size == 0:
        print("Compressed file is empty.")
        return 0.0

    ratio = original_size / compressed_size
    print(f"Original size: {original_size} bytes")
    print(f"Compressed size: {compressed_size} bytes")
    print(f"Compression ratio: {ratio:.2f}")
    
    
    
def entropy(file_path: str):
    """
    Calculate the entropy of a file, measured in bits per byte.

    Parameters
    ----------
    file_path : str
        The path to the file to calculate entropy for.
    """
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    with open(file_path, 'rb') as f:
        data = f.read()

    if not data:
        return 0.0

    # Calculate frequency of each byte value (0-255)
    frequency = [0] * 256
    for byte in data:
        frequency[byte] += 1

    # Normalize frequencies
    total = len(data)
    probabilities = [freq / total for freq in frequency if freq > 0]

    # Calculate entropy
    entropy_value = -sum(p * math.log2(p) for p in probabilities)
    print(f"Entropy: {entropy_value:.2f}", "bits per byte")