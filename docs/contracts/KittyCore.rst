
KittyCore is KittyMinting
=========================

CryptoKitties: Collectible, breedable, and oh-so-adorable cats on the Ethereum blockchain.
The main CryptoKitties contract, keeps track of kittens so they don't wander around and get lost.



Public State Variables
----------------------

- ``newContractAddress <address>``: Set in case the core contract is broken and an upgrade is required


External Functions
------------------


setNewAddress(address _v2Address) external onlyCEO whenPaused
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Used to mark the smart contract as upgraded, in case there is a serious breaking bug. This method does nothing but keep track of the new contract and emit a message indicating that the new address is set. It's up to clients of this contract to update to the new contract address in that case. (This contract will be paused indefinitely if such an upgrade takes place.)

Parameters
""""""""""

- ``_v2Address <address>``: new address

Returns
"""""""

None

getKitty(uint256 _id) external view returns (bool isGestating, bool isReady, uint256 cooldownIndex, uint256 nextActionAt, uint256 siringWithId, uint256 birthTime, uint256 matronId, uint256 sireId, uint256 generation, uint256 genes)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns all the relevant information about a specific kitty.

Parameters
""""""""""

- ``_id <uint256>``: The ID of the kitty of interest.

Returns
"""""""

- ``isGestating <bool>``
- ``isReady <bool>``
- ``cooldownIndex <uint256>``
- ``nextActionAt <uint256>``
- ``siringWithId <uint256>``
- ``birthTime <uint256>``
- ``matronId <uint256>``
- ``sireId <uint256>``
- ``generation <uint256>``
- ``genes <uint256>``

unpause() public onlyCEO whenPaused
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Override unpause so it requires all external contract addresses to be set before contract can be unpaused. Also, we can't have newContractAddress set either, because then the contract was upgraded.

Parameters
""""""""""

None

Returns
"""""""

None

withdrawBalance() external onlyCFO
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Allows the CFO to capture the balance available to the contract.
Auction Fee와 breedWithAuto()로 인해 증가된 ETH. giveBirth의 보상으로 주기위한 잔액을 제외하고 남은 금액을 반환함.

Parameters
""""""""""

None

Returns
"""""""

None
