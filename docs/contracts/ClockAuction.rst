
ClockAuction
============

Clock auction for non-fungible tokens.





External Functions
------------------


ClockAuction(address _nftAddress, uint256 _cut)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Constructor creates a reference to the NFT ownership contract and verifies the owner cut is in the valid range.

Parameters
""""""""""

- ``_nftAddress <address>``: address of a deployed contract implementing the Nonfungible Interface.
- ``_cut <uint256>``: percent cut the owner takes on each auction, must be between 0-10,000.

Returns
"""""""

None

withdrawBalance()
^^^^^^^^^^^^^^^^^

Remove all Ether from the contract, which is the owner's cuts as well as any Ether sent directly to the contract address. Always transfers to the NFT contract, but can be called either by the owner or the NFT contract.

Parameters
""""""""""

None

Returns
"""""""

None

createAuction(uint256 _tokenId,uint256 _startingPrice,uint256 _endingPrice,uint256 _duration,address _seller)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Creates and begins a new auction.

Parameters
""""""""""

- ``_tokenId <uint256>``: ID of token to auction, sender must be owner.
- ``_startingPrice <uint256>``: Price of item (in wei) at beginning of auction.
- ``_endingPrice <uint256>``: Price of item (in wei) at end of auction.
- ``_duration <uint256>``: Length of time to move between starting price and ending price (in seconds).
- ``_seller <address>``: Seller, if not the message sender

Returns
"""""""

None

bid(uint256 _tokenId) payable
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Bids on an open auction, completing the auction and transferring ownership of the NFT if enough Ether is supplied.

Parameters
""""""""""

- ``_tokenId <uint256>``: ID of token to bid on.

Returns
"""""""

None

cancelAuction(uint256 _tokenId)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Cancels an auction that hasn't been won yet. Returns the NFT to original owner.

Parameters
""""""""""

- ``_tokenId <uint256>``: ID of token on auction.

Returns
"""""""

None

cancelAuctionWhenPaused(uint256 _tokenId)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Cancels an auction when the contract is paused. Only the owner may do this, and NFTs are returned to the seller. This should only be used in emergencies.

Parameters
""""""""""

- ``_tokenId <uint256>``: ID of the NFT on auction to cancel.

Returns
"""""""

None

getAuction(uint256 _tokenId) view returns (address seller, uint256 startingPrice, uint256 endingPrice, uint256 duration, uint256 startedAt)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns auction info for an NFT on auction.

Parameters
""""""""""

- ``_tokenId <uint256>``: ID of the NFT on auction.

Returns
"""""""

- ``seller <address>``
- ``startingPrice <uint256>``
- ``endingPrice <uint256>``
- ``duration <uint256>``
- ``startedAt <uint256>``

getCurrentPrice(uint256 _tokenId) view returns (uint256)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the current price of an auction.

Parameters
""""""""""

- ``_tokenId <uint256>``: ID of the token price we are checking.

Returns
"""""""

- ``<uint256>``
