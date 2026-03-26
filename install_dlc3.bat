:: Script for installing dlc3. 
:: Source: https://github.com/DeepLabCut/DeepLabCut/issues/3219#issuecomment-3985962875
:: Author: Gilberto Vite. March 2025
:: Note: open the terminal as administrator to run this script.

@echo off
echo -----------------------------------------------
echo STARTING DEEPLABCUT SETUP
echo -----------------------------------------------
:: 1. Ask the user for the environment name
set /p ENV_NAME=Enter the name for your new environment (e.g., deeplabcut3): 

:: 2. Set default if input is empty
if "%ENV_NAME%"=="" (
    set ENV_NAME=DEEPLABCUT
    echo No name entered. Using default: DEEPLABCUT
)

echo.
echo Proceeding to create environment: %ENV_NAME%
echo -----------------------------------------------

:: 3. Create the Environment
call conda create -n %ENV_NAME% python=3.12 -y

:: 4. Activate Environment
call conda activate %ENV_NAME%

:: 5. Install Dependencies
echo Installing Core Libraries...
pip install -v "pandas[hdf5,performance]<3.0"
pip install "npe2==0.8.1"
pip install "pydantic>2"

:: 6. PyTorch for modern GPUs (CUDA 12.8)
echo Installing PyTorch (cu128)...
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu128

:: 7. DeepLabCut and GUI
echo Installing DeepLabCut and Napari...
pip install --pre deeplabcut[gui]
pip install -v "napari==0.6.6"
pip install napari-deeplabcut

:: 8. Verification
echo -----------------------------------------------
echo VERIFYING GPU ACCELERATION IN %ENV_NAME%
echo -----------------------------------------------
python -c "import torch; print('SUCCESS: CUDA Available') if torch.cuda.is_available() else print('FAILURE: CUDA Not Found')"

echo -----------------------------------------------
echo SETUP COMPLETE. Launching DeepLabCut...
echo -----------------------------------------------
python -m deeplabcut

pause