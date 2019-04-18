
KittyOwnership is KittyBase, ERC721
===================================

The facet of the CryptoKitties core contract that manages ownership, ERC-721 (draft) compliant.


Constants
---------

- ``name <string>``
- ``symbol <string>``
- ``InterfaceSignature_ERC165 <bytes4>``
- ``InterfaceSignature_ERC721 <bytes4>``

Public State Variables
----------------------

- ``erc721Metadata <ERC721Metadata>``: The contract that will return kitty metadata


External Functions
------------------


supportsInterface(bytes4 _interfaceID) external view returns (bool)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Introspection interface as per ERC-165 (https://github.com/ethereum/EIPs/issues/165). Returns true for any standardized interfaces implemented by this contract. We implement ERC-165 (obviously!) and ERC-721.

Parameters
""""""""""

- ``_interfaceID <bytes4>``

Returns
"""""""

- ``<bool>``

setMetadataAddress(address _contractAddress) public onlyCEO
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Set the address of the sibling contract that tracks metadata. CEO only.

Parameters
""""""""""

- ``_contractAddress <address>``

Returns
"""""""

None

balanceOf(address _owner) public view returns (uint256 count)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the number of Kitties owned by a specific address.

Parameters
""""""""""

- ``_owner <address>``: The owner address to check.

Returns
"""""""

- ``count <uint256>``

transfer(address _to, uint256 _tokenId) external whenNotPaused
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Transfers a Kitty to another address. If transferring to a smart contract be VERY CAREFUL to ensure that it is aware of ERC-721 (or CryptoKitties specifically) or your Kitty may be lost forever. Seriously.

Parameters
""""""""""

- ``_to <address>``: The address of the recipient, can be a user or contract.
- ``_tokenId <uint256>``: The ID of the Kitty to transfer.

Returns
"""""""

None

approve(address _to, uint256 _tokenId) external whenNotPaused
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Grant another address the right to transfer a specific Kitty via transferFrom(). This is the preferred flow for transfering NFTs to contracts.

Parameters
""""""""""

- ``_to <address>``: The address to be granted transfer approval. Pass address(0) to clear all approvals.
- ``_tokenId <uint256>``: The ID of the Kitty that can be transferred if this call succeeds.

Returns
"""""""

None

transferFrom(address _from, address _to, uint256 _tokenId) external whenNotPaused
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Transfer a Kitty owned by another address, for which the calling address has previously been granted transfer approval by the owner.

Parameters
""""""""""

- ``_from <address>``: The address that owns the Kitty to be transfered.
- ``_to <address>``: The address that should take ownership of the Kitty. Can be any address, including the caller.
- ``_tokenId <uint256>``: The ID of the Kitty to be transferred.

Returns
"""""""

None

totalSupply() public view returns (uint)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the total number of Kitties currently in existence.

Parameters
""""""""""

None

Returns
"""""""

- ``<uint256>``

ownerOf(uint256 _tokenId) external view returns (address owner)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the address currently assigned ownership of a given Kitty.

Parameters
""""""""""

- ``_tokenId <uint256>``

Returns
"""""""

- ``owner <address>``

tokensOfOwner(address _owner) external view returns(uint256[] ownerTokens)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns a list of all Kitty IDs assigned to an address.
This method MUST NEVER be called by smart contract code. First, it's fairly expensive (it walks the entire Kitty array looking for cats belonging to owner), but it also returns a dynamic array, which is only supported for web3 calls, and not contract-to-contract calls.

Parameters
""""""""""

- ``owner <address>``

Returns
"""""""

- ``ownerTokens <uint256[]>``

tokenMetadata(uint256 _tokenId, string _preferredTransport) external view returns (string infoUrl)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns a URI pointing to a metadata package for this token conforming to ERC-721 (https://github.com/ethereum/EIPs/issues/721)

Parameters
""""""""""

- ``_tokenId <uint256>``: The ID number of the Kitty whose metadata should be returned.
- ``_preferredTransport <string>``

Returns
"""""""

- ``infoUrl <string>``
