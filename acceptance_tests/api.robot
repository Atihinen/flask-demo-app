*** Settings ***
Library    SeleniumLibrary
Library    RequestsLibrary
Library    lib/XMLParserLib.py
Suite Setup    Get Movie And Open Browser
Suite Teardown    Close Browser

*** Variables ***
${SERVER}=    http://localhost:5000
${BROWSER}=    firefox
${FINNKINO_SCHEDULE}=    finnkino

*** Test Cases ***

Check That Movie Is Found From Correct Area
    Choose Lappeenranta From Area List
	Verify That Correct Movie Is Found

*** Keywords ***

Get Movie And Open Browser
	Create Session    ${FINNKINO_SCHEDULE}    http://www.finnkino.fi/xml/Schedule/
	${resp}=    Get Request   ${FINNKINO_SCHEDULE}    /?area=1041
	${movie_title}=    Get Movie Title    ${resp.content}
	Set Suite Variable    ${MOVIE_TITLE}    ${movie_title}
	Open Browser    ${SERVER}    ${BROWSER}

Ensure That Loader Gif Is Disabled
	Wait Until Element Is Not Visible    id=loader    10

Ensure That Loader Gif Is Enabled
	Wait Until Element Is Visible    id=loader    10

Choose Lappeenranta From Area List
	Select From List By Value    id=choose_theatre    1041

Verify That Correct Movie Is Found
	[Documentation]    MOVIE_TITLE variable is defined in suite setup
	Wait Until Keyword Succeeds    3x    2s    Page Should Contain    ${MOVIE_TITLE}