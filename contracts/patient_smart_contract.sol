// SPDX-License-Identifier: GPL-3.0
// final implementation of the smart contract

pragma solidity  >=0.7.0 < 0.9.0;

contract patient_vault{

    struct data_struct {

        string patient_name1;
    }   

    data_struct data_curr;

    function AddVals(string memory st1) public {
        data_curr = data_struct(st1);
    }

    function GetVal1() public view returns (string memory){

        return data_curr.patient_name1; 
    
    }
 
}