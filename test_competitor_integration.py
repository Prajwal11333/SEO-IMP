#!/usr/bin/env python3
"""
Test script for Competitor Analysis Integration
This script tests the competitor analysis service endpoints
"""

import requests
import json
import time
import sys

def test_health_check():
    """Test if the competitor analysis service is running"""
    try:
        response = requests.get("http://localhost:8002/health", timeout=5)
        if response.status_code == 200:
            print("✅ Competitor Analysis Service is running")
            print(f"   Response: {response.json()}")
            return True
        else:
            print(f"❌ Health check failed: {response.status_code}")
            return False
    except requests.exceptions.RequestException as e:
        print(f"❌ Cannot connect to Competitor Analysis Service: {e}")
        return False

def test_proxy_health():
    """Test if the Node.js proxy is running"""
    try:
        response = requests.get("http://localhost:3001/health", timeout=5)
        if response.status_code == 200:
            print("✅ Node.js Proxy Server is running")
            print(f"   Response: {response.json()}")
            return True
        else:
            print(f"❌ Proxy health check failed: {response.status_code}")
            return False
    except requests.exceptions.RequestException as e:
        print(f"❌ Cannot connect to Node.js Proxy: {e}")
        return False

def test_competitor_analysis():
    """Test the competitor analysis endpoint"""
    print("\n🔍 Testing Competitor Analysis...")
    
    # Test data
    test_data = {
        "your_domain": "https://example.com",
        "keywords": ["seo tools", "analytics"],
        "competitors": None,
        "depth": 5  # Quick analysis
    }
    
    try:
        # Start analysis
        print("   Starting analysis...")
        response = requests.post(
            "http://localhost:3001/api/competitor-analysis/analyze",
            json=test_data,
            timeout=10
        )
        
        if response.status_code == 200:
            result = response.json()
            analysis_id = result.get("analysis_id")
            print(f"✅ Analysis started: {analysis_id}")
            
            # Poll for results
            print("   Polling for results...")
            for i in range(10):  # Poll for up to 20 seconds
                time.sleep(2)
                
                status_response = requests.get(
                    f"http://localhost:3001/api/competitor-analysis/status/{analysis_id}",
                    timeout=5
                )
                
                if status_response.status_code == 200:
                    status_data = status_response.json()
                    status = status_data.get("status")
                    progress = status_data.get("progress", 0)
                    
                    print(f"   Status: {status} ({progress}%)")
                    
                    if status == "completed":
                        print("✅ Analysis completed successfully!")
                        print(f"   Results: {json.dumps(status_data.get('results', {}), indent=2)}")
                        return True
                    elif status == "failed":
                        print(f"❌ Analysis failed: {status_data.get('error', 'Unknown error')}")
                        return False
                else:
                    print(f"❌ Status check failed: {status_response.status_code}")
                    return False
            
            print("⏰ Analysis timed out")
            return False
            
        else:
            print(f"❌ Analysis start failed: {response.status_code}")
            print(f"   Response: {response.text}")
            return False
            
    except requests.exceptions.RequestException as e:
        print(f"❌ Analysis test failed: {e}")
        return False

def main():
    """Run all tests"""
    print("=" * 70)
    print("🧪 COMPETITOR ANALYSIS INTEGRATION TEST")
    print("=" * 70)
    
    # Test 1: Health checks
    print("\n1️⃣ Testing Service Health...")
    competitor_healthy = test_health_check()
    proxy_healthy = test_proxy_health()
    
    if not competitor_healthy or not proxy_healthy:
        print("\n❌ Services are not running properly")
        print("   Make sure to start:")
        print("   - Competitor Analysis: cd backend/python-service/Competitor && python app.py")
        print("   - Node.js Proxy: cd backend/node-server/node-Server && node Server.js")
        return False
    
    # Test 2: Competitor Analysis
    print("\n2️⃣ Testing Competitor Analysis...")
    analysis_success = test_competitor_analysis()
    
    # Summary
    print("\n" + "=" * 70)
    print("📊 TEST SUMMARY")
    print("=" * 70)
    
    if competitor_healthy and proxy_healthy and analysis_success:
        print("✅ ALL TESTS PASSED!")
        print("   Competitor Analysis integration is working correctly")
        return True
    else:
        print("❌ SOME TESTS FAILED")
        print("   Check the error messages above")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
