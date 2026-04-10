cat > /addons/poe-display/run.sh << 'EOF'
#!/usr/bin/with-contenv bashio
python3 /display.py
EOF
chmod +x /addons/poe-display/run.sh