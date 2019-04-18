
SiringClockAuction is ClockAuction
==================================

Reverse auction modified for siring.
We omit a fallback function to prevent accidental sends to this contract.



Public State Variables
----------------------

- ``isSiringClockAuction <bool>``: Sanity check that allows us to ensure that we are pointing to the right auction in our setSiringAuctionAddress() call.


External Functions
------------------


SiringClockAuction(address _nftAddr, uint256 _cut) public ClockAuction(_nftAddr, _cut)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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

Creates and begins a new auction. Since this function is wrapped, require sender to be KittyCore contract.

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

Places a bid for siring. Requires the sender is the KittyCore contract because all bid methods should be wrapped. Also returns the kitty to the seller rather than the winner.

Parameters
""""""""""

- ``_tokenId <uint256>``

Returns
"""""""

None
