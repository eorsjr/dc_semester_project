from typing import List, Tuple

class LZ77:
    """
    LZ77 compression and decompression class.

    Attributes
    ----------
    window_size : int, optional
        The size of the sliding window for compression (default is 20).
    """

    def __init__(self, window_size: int = 20):
        """
        Initialize the LZ77 compressor with a specified window size.

        Parameters
        ----------
        window_size : int, optional
            The size of the sliding window (default is 20).
        """
        self.window_size = window_size

    def compress(self, data: bytes) -> List[Tuple[int, int, int]]:
        """
        Compress the given data using the LZ77 algorithm.

        Parameters
        ----------
        data : bytes
            The input data to be compressed.

        Returns
        -------
        List[Tuple[int, int, int]]
            A list of tuples representing (offset, length, next_byte) for each compressed segment.
        """
        i = 0 # Initialize the current position in the data
        output = [] # Initialize the output list

        while i < len(data): # While there is data to process
            match = (0, 0) # Initialize the match as (distance, length)
            
            # Search for the longest match in the sliding window
            for j in range(max(0, i - self.window_size), i):
                length = 0
                # Find the longest matching substring
                while (length < self.window_size and
                       j + length < i and
                       i + length < len(data) and
                       data[j + length] == data[i + length]):
                    length += 1
                # Update match if a longer one is found
                if length > match[1]:
                    match = (i - j, length)

            # If a match is found, calculate the next byte
            if match[1] > 0:
                if i + match[1] < len(data):
                    next_byte = data[i + match[1]]
                    output.append((match[0], match[1], next_byte))
                    i += match[1] + 1
                else:
                    # Handle the end of data
                    output.append((match[0], match[1], -1))
                    break
            else:
                # No match found, store the literal byte
                output.append((0, 0, data[i]))
                i += 1

        return output

    def decompress(self, compressed_data: List[Tuple[int, int, int]]) -> bytes:
        """
        Decompress the given compressed data using the LZ77 algorithm.

        Parameters
        ----------
        compressed_data : List[Tuple[int, int, int]]
            A list of compressed (offset, length, next_byte) tuples.

        Returns
        -------
        bytes
            The decompressed original data.
        """
        output = bytearray()

        for offset, length, next_byte in compressed_data: # Iterate through the compressed data
            if offset == 0 and length == 0:
                # Directly append literal byte when no match
                output.append(next_byte)
            else:
                # Append the matched sequence from the sliding window
                start = len(output) - offset
                for j in range(length):
                    output.append(output[start + j])
                # Append the next byte if valid
                if next_byte != -1:
                    output.append(next_byte)

        return bytes(output)