  // SPDX-License-Identifier: MIT
  pragma solidity ^0.8.0;

  contract URLClickTracker {
      mapping(string => uint256) public urlClicks;

      function recordClick(string memory shortCode) public {
          urlClicks[shortCode]++;
      }

      function getClickCount(string memory shortCode) public view returns (uint256) {
          return urlClicks[shortCode];
      }
  }
