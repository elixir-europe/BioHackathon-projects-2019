import React from 'react';
import styled from 'styled-components';
import {QuackVote} from '../QuackVote';

const Card = styled.div`
    height: 400px;
    width: 800px;
    margin: 1rem;
    border-radius: 5px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    background-color: #eee;
    color: black;
`
const TitleContentWrapper = styled.div`
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
`
const CardTitle = styled.h1`
    padding-left: 1rem;
    padding-right: 1rem;
    padding-bottom: 0.5rem;
    font-style: bold;
    font-size: 1.2rem;
    font-family: Dosis;
    padding-bottom: 0px;
    .a{
    color: red;
    }
`
const CardAddInformation = styled.div`
    font-size: 0.8rem;
    padding-left: 1rem;
    padding-right: 1rem;

`
const CardContent = styled.div`
    border-radius: 5px;
    padding-top: 0.5rem;
    padding-left: 1rem;
    padding-right: 1rem;
    text-align: justify;

`
const CardBottom = styled.div`
      background-color: #dedede;
      padding-bottom: 0.5rem;
`

const A = styled.a`
    color: blue;
    text-decoration: none;
    :hover{
        color: #FF6F2F;
    }
    
`

var truncate = function (s, n) {
    // truncate a string with an ellipsis
    if (s.length > n) {
        return s.substr(0, n-3) + '...';
    } else {
        return s;
    }
};

const QuackCard = ({data}) => {
    return (
        <Card className={"card"}>
            <TitleContentWrapper>
                <CardTitle><A target='_blank' href={data.seeAlso}>{data.title}</A></CardTitle>
                <CardAddInformation>
                    (2019) doi: <a href={data.seeAlso}>{data.doi}</a>
                </CardAddInformation>
                <CardContent>
                    {truncate(data.abstract,1700)}
                </CardContent>
            </TitleContentWrapper>
        </Card>
    );
};

export default QuackCard;