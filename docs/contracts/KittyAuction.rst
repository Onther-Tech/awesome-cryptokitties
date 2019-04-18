
KittyAuction is KittyBreeding
=============================

Handles creating auctions for sale and siring of kitties. This wrapper of ReverseAuction exists only so that users can create auctions with only one transaction.





External Functions
------------------


setSaleAuctionAddress(address _address) external onlyCEO
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sets the reference to the sale auction.

Parameters
""""""""""

- ``_address <address>``: Address of sale contract.

Returns
"""""""

None

setSiringAuctionAddress(address _address) external onlyCEO
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sets the reference to the siring auction.

Parameters
""""""""""

- ``_address <address>``: Address of siring contract.

Returns
"""""""

None

function createSaleAuction(uint256 _kittyId, uint256 _startingPrice, uint256 _endingPrice, uint256 _duration) whenNotPaused
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Put a kitty up for auction. Does some ownership trickery to create auctions in one tx.

Parameters
""""""""""

- ``_kittyId <uint256>``
- ``_startingPrice <uint256>``
- ``_endingPrice <uint256>``
- ``_duration <uint256>``

Returns
"""""""

None

function createSiringAuction(uint256 _kittyId, uint256 _startingPrice, uint256 _endingPrice, uint256 _duration) whenNotPaused
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Put a kitty up for auction to be sire. Performs checks to ensure the kitty can be sired, then delegates to reverse auction.

Parameters
""""""""""

- ``_kittyId <uint256>``
- ``_startingPrice <uint256>``
- ``_endingPrice <uint256>``
- ``_duration <uint256>``

Returns
"""""""

None

bidOnSiringAuction(uint256 _sireId, uint256 _matronId) external payable whenNotPaused
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Completes a siring auction by bidding. Immediately breeds the winning matron with the sire on auction.

Parameters
""""""""""

- ``_sireId <uint256 >``: ID of the sire on auction.
- ``_matronId <uint256 >``: ID of the matron owned by the bidder.

Returns
"""""""

None

withdrawAuctionBalances() external onlyCLevel
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Transfers the balance of the sale auction contract to the KittyCore contract. We use two-step withdrawal to prevent two transfer calls in the auction bid function.

Parameters
""""""""""

None

Returns
"""""""

None
