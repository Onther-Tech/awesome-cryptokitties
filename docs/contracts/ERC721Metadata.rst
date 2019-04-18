
ERC721Metadata
==============

The external contract that is responsible for generating metadata for the kitties, it has one function that will return the data as bytes.





External Functions
------------------


getMetadata(uint256 _tokenId, string) public view returns (bytes32[4] buffer, uint256 count)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Given a token Id, returns a byte array that is supposed to be converted into string.

Parameters
""""""""""

- ``_tokenId <uint256>``
- ``<string>``

Returns
"""""""

- ``buffer <bytes32[4]>``
- ``count <uint256>``
