
ClockAuctionBase
================

Contains models, variables, and internal methods for the auction.

Struct
------

Auction
^^^^^^^

Represents an auction on an NFT

Members
"""""""
- ``seller <address>``: Current owner of NFT
- ``startingPrice <uint128>``: Price (in wei) at beginning of auction
- ``endingPrice <uint128>``: Price (in wei) at end of auction
- ``duration <uint64>``: Duration (in seconds) of auction
- ``startedAt <uint64>``: Time when auction started



Events
------

AuctionCreated(uint256 tokenId, uint256 startingPrice, uint256 endingPrice, uint256 duration)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^



Parameters
""""""""""

- ``tokenId <uint256>``
- ``startingPrice <uint256>``
- ``endingPrice <uint256>``
- ``duration <uint256>``

AuctionSuccessful(uint256 tokenId, uint256 totalPrice, address winner)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^



Parameters
""""""""""

- ``tokenId <uint256>``
- ``totalPrice <uint256>``
- ``winner <address>``

AuctionCancelled(uint256 tokenId)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^



Parameters
""""""""""

- ``tokenId <uint256>``

