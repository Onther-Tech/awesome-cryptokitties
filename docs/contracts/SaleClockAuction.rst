
SaleClockAuction is ClockAuction
================================

Clock auction modified for sale of kitties
We omit a fallback function to prevent accidental sends to this contract.



Public State Variables
----------------------

- ``isSaleClockAuction <bool>``: Sanity check that allows us to ensure that we are pointing to the right auction in our setSaleAuctionAddress() call.
- ``gen0SaleCount <uint256>``: Tracks last 5 sale price of gen0 kitty sales
- ``lastGen0SalePrices <uint256[5]>``: Tracks last 5 sale price of gen0 kitty sales


External Functions
------------------


SaleClockAuction(address _nftAddr, uint256 _cut) public ClockAuction(_nftAddr, _cut)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Delegate constructor

Parameters
""""""""""

- ``_nftAddr <address>``
- ``_cut <uint256>``

Returns
"""""""

None

createAuction(uint256 _tokenId, uint256 _startingPrice, uint256 _endingPrice, uint256 _duration, address _seller) external
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Creates and begins a new auction.

Parameters
""""""""""

- ``_tokenId <uint256>``: ID of token to auction, sender must be owner.
- ``_startingPrice <uint256>``: Price of item (in wei) at beginning of auction.
- ``_endingPrice <uint256>``: Price of item (in wei) at end of auction.
- ``_duration <uint256>``: Length of auction (in seconds).
- ``_seller <address>``: Seller, if not the message sender

Returns
"""""""

None

bid(uint256 _tokenId) external payable
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Updates lastSalePrice if seller is the nft contract Otherwise, works the same as default bid method.

Parameters
""""""""""

- ``_tokenId <uint256>``

Returns
"""""""

None

averageGen0SalePrice() external view returns (uint256)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^



Parameters
""""""""""

None

Returns
"""""""

- ``<uint256>``
