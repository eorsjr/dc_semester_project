from typing import List, Tuple

class LZ78:
    """
    LZ78 compression and decompression class.

    Methods
    -------
    compress(data: bytes) -> List[Tuple[int, bytes]]
        Compresses the given data using the LZ78 algorithm.
    decompress(compressed_data: List[Tuple[int, bytes]]) -> bytes
        Decompresses the given data using the LZ78 algorithm.
    """

    def compress(self, data: bytes) -> List[Tuple[int, bytes]]:
        """
        Compress the given data using the LZ78 algorithm.

        Parameters
        ----------
        data : bytes
            The input data to be compressed.

        Returns
        -------
        List[Tuple[int, bytes]]
            A list of tuples representing (index, next_byte) for each compressed segment.
        """
        dictionary = {b'': 0} # Initialize the dictionary with an empty string
        output = [] # Initialize the output list
        prefix = b'' # Initialize the prefix
        index = 1 # Initialize the index for the next prefix

        for byte in data:
            prefix += bytes([byte]) # Append the current byte to the prefix
            if prefix not in dictionary:
                output.append((dictionary[prefix[:-1]], bytes([byte]))) # Append the index of the previous prefix and the current byte
                dictionary[prefix] = index # Add the new prefix to the dictionary
                index += 1 # Increment the index for the next prefix
                prefix = b'' # Reset the prefix for the next iteration

        if prefix: # If there is any remaining prefix
            output.append((dictionary[prefix[:-1]], prefix[-1:])) # Append the index of the previous prefix and the last byte of the prefix

        return output

    def decompress(self, compressed_data: List[Tuple[int, bytes]]) -> bytes:
        """
        Decompress the given data using the LZ78 algorithm.

        Parameters
        ----------
        compressed_data : List[Tuple[int, bytes]]
            A list of tuples representing (index, next_byte) for each compressed segment.

        Returns
        -------
        bytes
            The decompressed original data.
        """

        if not compressed_data:
            return bytes()

        dictionary = {0: b''} # Initialize the dictionary with an empty string
        output = bytearray() # Initialize the output bytearray
        index = 1 # Initialize the index for the next prefix

        for idx, byte in compressed_data: # Iterate over each compressed segment
            
            entry = dictionary.get(idx, b'') + byte # Get the existing entry from the dictionary and append the next byte
            output.extend(entry) # Append the entry to the output
            dictionary[index] = entry # Add the new entry to the dictionary
            index += 1 # Increment the index for the next prefix

        return bytes(output) # Return the output as bytes
